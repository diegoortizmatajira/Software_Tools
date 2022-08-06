class MenuOption:

    def __init__(self, shortcut: str, text: str, function) -> None:
        self.shortcut = shortcut
        self.text = text
        self.function = function


class Base:

    def print_warning(self, message: str):
        self.separator('*')
        print(f'>> {message}')
        self.separator('*')

    def print_error(self, message: str):
        self.separator('*')
        print(f'Error: {message}')
        self.separator('*')

    def print(self, message: str):
        print(f'{message}')

    def input(self, message: str) -> str:
        return input(message)

    def separator(self, character: str):
        print(character * 50)

    def menu(self, *options: MenuOption):
        while True:
            self.separator('=')
            for option in options:
                print(f'[{option.shortcut}] - {option.text}')
                print(f'[q] - Quit')
            selected = self.input('Please select an option...')
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
