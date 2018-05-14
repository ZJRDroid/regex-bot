from telegram.ext import Filters
from telegram.ext import BaseFilter

class _Reply_text(BaseFilter):
    name = 'Filters.reply_text'

    def filter(self, message):
        if message.reply_to_message:
            return bool(message.reply_to_message.text or message.reply_to_message.caption)
        return False

Filters.reply_text = _Reply_text()
