import logging
import importlib
from telegram.ext.dispatcher import run_async
from bot import updater
from bot import dispatcher

logging.basicConfig(format='[%(asctime)s][%(name)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

@run_async
def error_callback(bot, update, error):
    pass # p-t-b's logger already logs this to the console

def main():
    for modname in ["sed", "help", "yesno"]:
        module = getattr(importlib.import_module('bot.modules.{}'.format(modname)), "module")
        logger.info("module imported: %s (handlers: %d)", module.name, len(module.handlers))
        for handler in module.handlers:
            dispatcher.add_handler(handler)

    dispatcher.add_error_handler(error_callback)

    updater.start_polling(clean=True)
    updater.idle()

if __name__ == '__main__':
    main()