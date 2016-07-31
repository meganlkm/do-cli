from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.algebra import GAPLexer
from pygson.json_lexer import JSONLexer

from do_cli.utils.json_helpers import pretty_print


def format_json(content):
    return highlight(
        pretty_print(content, sort_keys=False),
        JSONLexer(),
        Terminal256Formatter(style='solarized_dark256')
    ).strip()


def format_table(content):
    return highlight(
        content,
        GAPLexer(),
        Terminal256Formatter(style='solarized_dark256')
    ).strip()
