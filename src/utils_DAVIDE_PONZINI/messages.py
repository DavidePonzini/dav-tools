import sys as _sys

from .text_color import TextFormatOption
from .text_color import print_colored_text as _print_colored_text
from .text_color import input_colored as _input_colored
from .text_color import clear_line as _clear_line


# generic and customizable message
def message(text, icon=None, text_options=[], icon_options=[], blink=False, end='\n', file=_sys.stderr):
    _clear_line()

    if icon is not None:
        _print_colored_text('[', *icon_options, TextFormatOption.Style.BOLD, end='', file=file)
        
        if blink:
            _print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, TextFormatOption.Style.BLINK, end='', file=file)
        else:
            _print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, end='', file=file)
        
        _print_colored_text(']', *icon_options, TextFormatOption.Style.BOLD, end='', file=file)
        _print_colored_text(' ', end='', file=file)
    
    _print_colored_text(text, *text_options, end=end, file=file)
    

# message indicating an information
def info(text: str, blink=False) -> None:
    message(text,
             icon='*',
             icon_options=[
                 TextFormatOption.Color.BLUE
             ], 
             blink=blink)

# message indicating an error
def error(text: str, blink=False) -> None:
    message(text, 
             icon='-', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.RED
             ]
    )

# message indicating a critical error. The program terminates after showing this message
def critical_error(text: str, blink=False, exit_code=1) -> None:
    message(text, 
             icon='x', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.RED
             ],
             text_options=[
                 TextFormatOption.Color.RED
             ]
    )

    _sys.exit(exit_code)

# message indicating a warning
def warning(text: str, blink=False) -> None:
    message(text, 
             icon='!', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.YELLOW
             ]
    )

# message indicating a successfully completed action
def success(text: str, blink=False) -> None:
    message(text, 
             icon='+', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.GREEN
             ]
    )

# prints a question and returns the answer
def ask(question: str, end=': ') -> str:
    message(f'{question}{end}',
             icon='?',
             icon_options=[
                 TextFormatOption.Color.BLUE
             ],
             end='')
    
    return _input_colored(
        TextFormatOption.Style.ITALIC,
    )

# prints a question asking the user if they want to continue executing the program
# 	a positive answer makes the program continues its normal execution
# 	a negative answer terminates the program
# optionally supports a custom question
def ask_continue(text: str=None):
    if text is not None:
        message = f'{text}. Continue? (y/N)'
    else:
        message = 'Continue? (y/N)'

    while True:
        ans = ask(message, end=' ')

        if ans.lower() == 'y':
            break
        if ans.lower() == 'n' or len(ans) == 0:
            _sys.exit()