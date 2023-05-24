import sys as _sys
from . import commands as _commands
from ._text_format import TextFormat


def get_format(*options):
    result = ''

    for option in options:
        result += option.decode()

    return result

def set_format(*options, file=_sys.stdout):
    for option in options:
        print(option.decode(), end='', file=file)

def get_colored_text(text: str, *format_options):
    result = ''
    result += get_format(*format_options)
    result += text
    result += get_format(TextFormat.RESET)

    return result

def print_colored_text(text: str, *format_options, end: str='\n', file=_sys.stdout):
    text = get_colored_text(text, *format_options)
    print(text, end=end, file=file)

def input_colored(*format_options):
    set_format(*format_options, file=_sys.stderr)
    result = input()
    set_format(TextFormat.RESET)

    return result

def clear_line(file=_sys.stdout):
    print('\r', ' ' * TextFormat.get_term_len(), '\r',
          sep='', end='', file=file)