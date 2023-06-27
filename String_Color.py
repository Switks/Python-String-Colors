#Colors for strings in terminals! :D
# All of the information was used from https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

class COLOR:
    #Fonts
    RESET = '\033[0m'
    ITALIZE = '\033[3m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\033[7m'
    CROSSLINE = '\033[9m'

    #RGB Colors
    def RGB(RED: int, GREEN: int, BLUE: int):
        if (RED < 0 or RED > 255) or (GREEN < 0 or GREEN > 255) or (BLUE < 0 or BLUE > 255):
            print(f"{COLOR.BRIGHT_RED}💀Invalid {COLOR.BOLD}RGB VALUE\n")
            pass
        return f'\033[38;2;{RED};{GREEN};{BLUE}m'
    
    #ID Colors
    def ID(ID:int):
        if ID > 255 or ID < 0:
            print(f"{COLOR.BRIGHT_RED}💀Invalid ID\n{COLOR.YELLOW}Use this table for reference! {COLOR.UNDERLINE}https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png{COLOR.RESET}")
            pass
        return f'\033[38;5;{ID}m'
    
    #Default Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    #Default Bright Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    #RGB Highlights
    def HIGH_RGB(RED: int, GREEN: int, BLUE: int):
        return f'\033[48;2;{RED};{GREEN};{BLUE}m'
    
    #ID Highlights
    def HIGHLIGHT_ID(ID:int):
        if ID > 255 or ID < 0:
            print(f"{COLOR.BRIGHT_RED}💀Invalid {COLOR.BOLD}COLOR ID\n{COLOR.YELLOW}Use this table for reference! {COLOR.UNDERLINE}https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png{COLOR.RESET}")
            pass
        return f'\033[48;5;{ID}m'

    #Default Highlights
    HIGHLIGHT_BLACK = '\033[40m'
    HIGHLIGHT_RED = '\033[41m'
    HIGHLIGHT_GREEN = '\033[42m'
    HIGHLIGHT_YELLOW = '\033[43m'
    HIGHLIGHT_BLUE = '\033[44m'
    HIGHLIGHT_MAGENTA = '\033[45m'
    HIGHLIGHT_CYAN = '\033[46m'
    HIGHLIGHT_WHITE = '\033[47m'
    
    #Default Bright Highlights
    BRIGHT_HIGHLIGHT_BLACK = '\033[100m'
    BRIGHT_HIGHLIGHT_RED = '\033[101m'
    BRIGHT_HIGHLIGHT_GREEN = '\033[102m'
    BRIGHT_HIGHLIGHT_YELLOW = '\033[103m'
    BRIGHT_HIGHLIGHT_BLUE = '\033[104m'
    BRIGHT_HIGHLIGHT_MAGENTA = '\033[105m'
    BRIGHT_HIGHLIGHT_CYAN = '\033[106m'
    BRIGHT_HIGHLIGHT_WHITE = '\033[107m'