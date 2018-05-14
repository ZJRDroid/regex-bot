import re
import logging

logger = logging.getLogger(__name__)

REGEX_FLAGS = "ilmsax"
FLAGS_DICT = {
    "i": re.I,
    "l": re.L,
    "m": re.M,
    "s": re.S,
    "a": re.A,
    "x": re.X
}

class Regex():
    def __init__(self, string, pattern, repl, flags=None):
        self.string = string
        self.pattern = pattern
        self.repl = repl
        self.count = 1 # by default, make just one replacement, unless the "g" flag is passed
        self.flags = 0 # default value for the "flags" argument of re.sub/re.subn 
        if flags:
            for flag in flags:
                logger.info("elaborating flag: %s", flag)
                flag_lower = flag.lower()
                if flag_lower == "g": # re.G: don't return after the first match
                    logger.info("<g> flag found")
                    self.count = 0 # passing count=0 to resub/re.subn will make it not return after the first match
                if flag_lower in REGEX_FLAGS:
                    self.flags |= FLAGS_DICT[flag_lower] # biwise-concatenete the re.FLAG object

    def subn(self, escape_html=False):
        return re.subn(
            self.pattern,
            self.repl,
            self.string,
            flags=self.flags,
            count=self.count
        )

    def sub(self, escape_html=False):
        return re.sub(
            self.pattern,
            self.repl,
            self.string,
            flags=self.flags,
            count=self.count
        )

