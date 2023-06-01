'''
user interface class: for now it's just in the console,
but later I will create a real nice-looking user interface.
'''
import os

class UI:
    def __init__(self) -> None:
        pass

    def display_menu(self):
        '''
        Displays main menu for the user, returns a integer choice.
        1. Add a new grad school (e.g. university of georgia)
        2. Add a new program (e.g. masters in electrical engineering)
        3. Search for a grad school in the database
        4. Mark a grad school as applied
        5. press q any time to quit

        '''
        # user's main menu
        print("Welcome to the grad school database.")
        print("Please choose an option by typing a number and pressing enter.")
        print("1. Add a new grad school (e.g. university of georgia)")
        print("2. Add a new program (e.g. masters in electrical engineering)")
        print("3. Search for a grad school in the database")
        print("4. Mark a grad school as applied")
        print("5. press q any time to quit")

        valid_choice = False
        while not valid_choice:
            choice = input()
            valid_choice = True

            match choice:
                case "1":
                    return "add school"
                case "2":
                    return "add program"
                case "3":
                    return "search school"
                case "4":
                    return "mark applied"
                case "5":
                    return "quit"
                case "q":
                    return "quit"
                case _:
                    print("Sorry, invalid choice. Please enter a number from 1 to 5: ")
                    valid_choice = False
            

    
    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')

    def get_school_name(self):
        return input("What is the name of the school? (e.g. Georgia Tech): ")
    
    def get_school_state(self):
        return input("In which state is the school located? (e.g. GA): ")
    
    def get_school_city(self):
        return input ("In which city is the school located? (e.g. Atlanta): ")
    
    def bad_input(self):
        print("Sorry, invalid choice. Please try again. ")

    def not_in_database(self, database_name):
        print(f"This was not found in the {database_name} database. Please try again. ")

    def confirm_add_to_database(self, addition, database_name):
        valid_choice = False

        while not valid_choice:
            y_n = input("You want to add {} to the {} database. Is this correct? (y/n): "
                        .format(addition, database_name))

            if y_n == "y" or y_n == "Y":
                return True
            if y_n == "n" or y_n == "N":
                return False
            else:
                self.bad_input()

    def adding_to_database(self):
        print("Adding to the database... ")
        input()

    def back_to_menu(self):
        print("Going back to main menu... ")
        input()


