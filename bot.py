import logging
import importlib

from bot import updater
from bot import dispatcher

logging.basicConfig(format='[%(asctime)s][%(name)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    for modname in ["sed", "help", "yesno"]:
        module = getattr(importlib.import_module('bot.modules.{}'.format(modname)), "module")
        logger.info("module imported: %s (handlers: %d)", module.name, len(module.handlers))
        for handler in module.handlers:
            dispatcher.add_handler(handler)

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main()
