import re

from telegram import Update
from telegram.ext import RegexHandler


class FilteredRegexHandler(RegexHandler):
    def __init__(self, *args, **kwargs):
        self.filters = kwargs.pop("filters")

        RegexHandler.__init__(self, *args, **kwargs)
    
    def check_update(self, update):
        if not isinstance(update, Update) and not update.effective_message:
            return False
        if self.filters:
            message = update.effective_message
            if isinstance(self.filters, list):
                res = any(func(message) for func in self.filters)
            else:
                res = self.filters(message)
            if not res:
                return False
        
        if any([self.message_updates and update.message,
                self.edited_updates and (update.edited_message or update.edited_channel_post),
                self.channel_post_updates and update.channel_post]) and \
                update.effective_message.text:
            match = re.match(self.pattern, update.effective_message.text)
            return bool(match)

        return False