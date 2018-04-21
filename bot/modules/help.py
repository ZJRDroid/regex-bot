import logging
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import ParseMode
from bot.customfilters import Filters
from bot import strings as s

logger = logging.getLogger(__name__)

extended_help_markup = InlineKeyboardMarkup([
	[InlineKeyboardButton("extended help", callback_data="extend")]
])

short_help_markup = InlineKeyboardMarkup([
	[InlineKeyboardButton("reduce", callback_data="reduce")]
])

@run_async
def help_message(bot, update):
	logger.info("/help or /start command")
	update.message.reply_markdown(s.help_short,
		reply_markup=extended_help_markup, disable_web_page_preview=True)

@run_async
def on_extended_help_button(bot, update):
	logger.info("extend help")
	update.callback_query.message.edit_text(s.help_extended,
		reply_markup=short_help_markup, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@run_async
def on_short_help_button(bot, update):
	logger.info("reduce help")
	update.callback_query.message.edit_text(s.help_short,
		reply_markup=extended_help_markup, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

class module:
	name = "help"
	handlers = (
		CommandHandler(["start", "help"], help_message, filters=Filters.private),
		CallbackQueryHandler(on_extended_help_button, pattern='^extend$'),
		CallbackQueryHandler(on_short_help_button, pattern='^reduce$'),
	)