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

        # get user input
        return input()
    
    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')

    def get_input(self):
        '''
        This function gets the input that the program wants.
        input options:
        adding stuff:
        - Add a career path
        - Add a school
        - Add a program
        accessing stuff
        - See what schools I have applied for
        - search database by category
        changing stuff
        - mark a program as applied
        - favorite a program
        - un-favorite a program
        other
        - Quit
        '''
        
        # first, take user to main menu
        main_menu_input = self.display_menu()
        
        # let them quit if they want
        if main_menu_input == "q" or main_menu_input == "5":
            return "quit"
        
        if main_menu_input == "1":

            # user wants to add a new grad school.
            valid_input = False

            while not valid_input:

                school_name = input("What is the name of the school? (e.g. Georgia Tech): ")

                state = input("in which state is this school located? (e.g. GA or Georgia): ")

                city = input("in which {} city is this school located? (e.g. Atlanta): ".format(state))

                add_school = input("you want to add {}: {}, {} to the database. Is this correct? (y/n): ".format(school_name,city,state))

                if add_school == "y":
                    print("adding to the database...")
                    input("Press enter to go back to main menu: ")
                    valid_input = True
                    return [ "new", "school", school_name, state ,city ]
                
                elif add_school == "n":
                    print("okay, I won't add this school. ")
                    try_again = input("please press 1 to try again or 2 to go back to main menu: ")
                    if try_again == "1":
                        print("Trying again...")
                    elif try_again == "2":
                        print("Going back to main menu... ")
                        valid_input = True
