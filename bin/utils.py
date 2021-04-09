from pygments import highlight, lexers, formatters
from json import dumps

def format_dict(object: dict) -> str:
    return(
        highlight(
            dumps(
                object, 
                indent=4
            ), 
            lexers.JsonLexer(), 
            formatters.TerminalFormatter()
        )
    )