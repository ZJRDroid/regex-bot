import logging
from html import escape as html_escape

from telegram.error import BadRequest
from telegram.constants import MAX_MESSAGE_LENGTH

from bot.customfilters import Filters
from bot.regexer import Regex
from bot.filteredregexhandler import FilteredRegexHandler

logger = logging.getLogger(__name__)

COMMAND_REGEX = r"^([s*]?/?)/((?:\\/|[^/])+)/((?:\\/|[^/])*)(?:/(.*))?"
MODES = {
    "": "<b>Did you mean:</b>\n{}",
    "s": "{}",
    "*": "*{}"
}


def get_response(mode, string):
    mode = mode.replace("/", "")
    return MODES[mode].format(html_escape(string))


def on_sed(_, update, groups):
    text = update.message.reply_to_message.text or update.message.reply_to_message.caption
    mode = groups[0]
    pattern = groups[1]
    replacement = groups[2].replace('\\/', '/')  # ??? https://github.com/SijmenSchoon/regexbot/blob/master/regexbot.py#L25
    flags = groups[3] if len(groups) > 3 else None
    logger.info(
        "\nmode: %s\ntext: %s\npattern: %s\nreplacement: %s\nflags: %s",
        mode,
        text,
        pattern,
        replacement,
        flags
    )
        
    regex = Regex(text, pattern, replacement, flags)

    try:            
        new_string, n_subs = regex.subn()
        logger.info("re.subn result:\nnew_string: %s\nn_subs: %d", new_string, n_subs)
    except Exception as e:
        logger.info("re.subn exception: %s", str(e), exc_info=True)
        # update.message.reply_text(s.oopsie_woopsie) # might be the user who fucked up the regex
        return  # don't proceed further

    if n_subs > 0:
        if len(new_string) > MAX_MESSAGE_LENGTH:
            logger.info("result too long: substringing...")
            new_string = new_string[:MAX_MESSAGE_LENGTH-16]  # -16: "*Did you mean:*\n"
        update.message.reply_to_message.reply_html(get_response(mode, new_string), disable_web_page_preview=True)
        if mode.endswith("/"):  # try to delete the command
            try:
                update.message.delete()
            except BadRequest as e:  # the bot doesn't have the permission to delete the message
                logger.info("exception while trying to delete a message: %s", e)


class module:
    name = "sed"
    handlers = (
        FilteredRegexHandler(COMMAND_REGEX, on_sed, pass_groups=True, filters=Filters.reply_text),
    )
