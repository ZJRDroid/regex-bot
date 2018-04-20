dym = "<b>Did you mean:</b>"
help_short = """\
Simple sed-like bot, using [Python's regular expressions](https://docs.python.org/3/howto/regex.html)

Usage: `s/pattern/replacement/flags` (flags are optional)

[source code](https://github.com/zeroone2numeral2/regex-bot)\
"""

help_extended = """\
*Avaliable commands flavours*:
`s/pattern/repl/flags`: returns simple replacement
`/pattern/repl/flags`: "_Did you mean:_" reply
`*/pattern/repl/flags`: returns replacement with a leading \*

Works just in reply of another message/media with caption. In groups, the bot will quote the replied-to message.

*Command deletion*:
replace the first / with a double / to force the bot to delete your message automatically \
(obviously, the bot must be granted the permission to delete messages)
Examples:
`s//pattern/replacement`
`//pattern/replacement`
`*//pattern/replacement`

*About flags*:
the third argument (flags) is optional.
You can use one or more flags - just pass the corresponding letter(s) \
([flags docs](https://docs.python.org/3/howto/regex.html#compilation-flags)).
You can also pass the `g` flag for the match to be global (do not stop after the first match).
Unknown flags will be ignored

*yes/no*
Write `y/n` or `yes/no` at the end of a message to get a random positive/negative answer from the bot\
"""

oopsie_woopsie = """OOPSIE WOOPSIE!! \
Uwu We made a fucky wucky!! \
A wittle fucko boingo! \
The code monkeys at our headquarters are working VEWY HAWD to fix this!\
"""

yesno_list = (
	'Yes.',
	'No.',
	'Absolutely.',
	'In your dreams.'
)