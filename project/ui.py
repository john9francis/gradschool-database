'''
user interface class: for now it's just in the console,
but later I will create a real nice-looking user interface.
'''
import os

class UI:
    def __init__(self) -> None:
        pass

    def display_menu(self):
        '''Displays main menu for the user, returns a integer choice.'''
        # user's main menu
        print("Welcome to the grad school database.")
        print("Please choose an option by typing a number and pressing enter.")
        print("1. Add a new grad school (e.g. university of georgia)")
        print("2. Add a new program (e.g. masters in electrical engineering)")
        print("3. Search for a grad school in the database")
        print("4. Mark a grad school as applied")
        print("5. press q any time to quit")

        # get user input
        return input()
    
    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')