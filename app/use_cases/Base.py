from colorama import Fore, Style


class MenuOption:

    def __init__(self, shortcut: str, text: str, function) -> None:
        self.shortcut = shortcut
        self.text = text
        self.function = function


class Base:

    def print_warning(self, message: str):
        self.separator('*', Fore.YELLOW)
        self.print(f'>> {message}', Fore.YELLOW)
        self.separator('*', Fore.YELLOW)

    def print_error(self, message: str):
        self.separator('*', Fore.RED)
        self.print(f'Error: {message}', Fore.RED)
        self.separator('*', Fore.RED)

    def print_success(self, message: str):
        self.separator('-', Fore.GREEN)
        self.print(f'{message}', Fore.GREEN)
        self.separator('-', Fore.GREEN)

    def print(self, message: str, color=Style.RESET_ALL, padding=1):
        print(f'{" "*padding}{color}{message}{Style.RESET_ALL}')

    def header(self, title: str, padding: int = 1):
        print('\n' * padding)
        self.separator('=', Fore.BLUE)
        self.print(title)
        self.separator('=', Fore.BLUE)

    def input(self, message: str) -> str:
        return input(message)

    def separator(self, character: str, color=Style.RESET_ALL):
        self.print(f'{color}{character * 50}{Style.RESET_ALL}', padding=0)

    def menu(self, title: str, *options: MenuOption):
        while True:
            self.header(title)
            for option in options:
                self.print(f'[{option.shortcut}] - {option.text}')
            self.print(f'[q] - Quit')
            selected = self.input('\nPlease select an option...')
            if selected == 'q':
                return
            for option in options:
                if option.shortcut == selected:
                    # Executes the function for the option
                    option.function()
                    break
            else:
                # If no option matches, then show a warning
                self.print_warning(
                    f'The option "{selected}" is invalid, try again..')
