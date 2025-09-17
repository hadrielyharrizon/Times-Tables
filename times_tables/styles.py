from colorama import Fore, Style, init

init(autoreset=True)

STYLES = {
    "show": Fore.CYAN,
    "nome": Fore.MAGENTA,
    "idade": Fore.RED,
    "normal": Fore.WHITE,
}

def styled(text, style="normal"):
    return f"{STYLES.get(style, Fore.WHITE)}{text}{Style.RESET_ALL}"

def c_show(text): return styled(text, "show")
def c_nome(text): return styled(text, "nome")
def c_idade(text): return styled(text, "idade")