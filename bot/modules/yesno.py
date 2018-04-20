import logging
from random import choice
from telegram.ext.dispatcher import run_async
from telegram.ext import RegexHandler
from bot.customfilters import Filters
from bot import strings as s

logger = logging.getLogger(__name__)

YESNO_REGEX = r".*(?:y(?:es)?\/no?|no?\/y(?:es)?)$"

@run_async
def on_yesno(bot, update):
	logger.info("yes/no")
	reply = choice(s.yesno_list)
	update.message.reply_text(reply)

class module:
	name = "yesno"
	handlers = (
		RegexHandler(YESNO_REGEX, on_yesno),
	)