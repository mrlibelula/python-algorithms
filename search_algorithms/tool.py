import time

def color(clr='GRAY'):
    clr = clr.upper()
    colors = {
        "DARKGRAY": "\033[90m", 
        "RED": "\033[91m", 
        "GREEN": "\033[92m", 
        "YELLOW": "\033[93m", 
        "PURPLE": "\033[94m", 
        "PINK": "\033[95m", 
        "CYAN": "\033[96m", 
        "WHITE": "\033[97m",
        "DARKRED": "\033[31m",
        "DARKGREEN": "\033[32m",
        "DARKYELLOW": "\033[33m",
        "DARKBLUE": "\033[34m",
        "DARKPINK": "\033[35m",
        "DARKCYAN": "\033[36m",
        "GRAY": "\033[37m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
    }
    return colors[clr] if clr in colors else colors['GRAY']

# decorator
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        purple = color('PURPLE')
        gray = color()
        print(f"{purple}{func.__name__} took {str((end - start) * 1000)} ms{gray}")
        return result
    return wrapper