import colorama

class Colors():
    DEFAULT = colorama.Style.RESET_ALL
    WARNING = colorama.Fore.YELLOW
    INFO = colorama.Fore.LIGHTBLUE_EX
    ERROR = colorama.Fore.RED 
    SUCCESS = colorama.Fore.GREEN 

class Icons():
    DEFAULT = f"{Colors.DEFAULT}[*]"
    WARNING = f"{Colors.WARNING}[!]"
    INFO = f"{Colors.INFO}[?]"
    ERROR = f"{Colors.ERROR}[-]"
    SUCCESS = f"{Colors.SUCCESS}[+]"

class Error():
    ERROR_MESSAGE = f"{Icons.WARNING} A execução encontrou o seguinte erro:\n"
    
    def get_exception_message(error):
        EXCEPTION_MESSAGE = f"{Error.ERROR_MESSAGE}{Icons.ERROR} {error}{Colors.DEFAULT}\n"
        return EXCEPTION_MESSAGE
