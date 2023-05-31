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

                city = input("in which city is this school located? (e.g. Atlanta): ")

                state = input("in which state is this school located? (e.g. GA): ")

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
