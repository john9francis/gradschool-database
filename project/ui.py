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
        print("2. Add a new Career Path (e.g. software engineer)")
        print("3. Add a new program (e.g. masters in electrical engineering)")
        print("4. Search programs by state")
        print("5. Search programs by career path")
        print("6. press q any time to quit")

        valid_choice = False
        while not valid_choice:
            choice = input()
            valid_choice = True

            match choice:
                case "1":
                    return "add school"
                case "2":
                    return "add career path"
                case "3":
                    return "add program"
                case "4":
                    return "search program by state"
                case "5":
                    return "search program by career"
                case "6":
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
    
    def get_state(self):
        return input("Please enter state (e.g. GA): ")
    
    def get_city(self):
        return input ("Please enter city (e.g. Atlanta): ")
    
    def get_new_career_path(self):
        return input("What is the name of your new career path? (e.g. Software developer): ")
    
    def get_career_path(self):
        return input("Please enter career path: ")
    
    def get_program_name(self):
        return input("What is the name of the program the school offers? (e.g. MS in computer science): ")

    def user_input_to_continue(self):
        print()
        return input("Press enter to continue: ")
    
    def displaying_programs_in_category(self, category):
        print(f"Here all your saved grad programs in {category}: ")
        print()

    
    def display_program_with_school(self, program, school):
        ''' e.g. "MS in engineering at Harvard"'''
        print(f"{program} at {school}")
    
    def choose_for_program(self, category, schools):
        print()
        print(f"Which {category} offers this program? ")
        print("Options:")
        for school in schools:
            print(school)

        return input("(Type your answer here): ")
    
    def choose_career_path(self, career_paths):
        print()
        print("Which career path?")
        print("Options: ")
        print()
        for career in career_paths:
            print(career)

        print()
        return input("(Type your answer here): ")


    def bad_input(self):
        print("Sorry, invalid choice. Please try again. ")

    def not_in_database(self, database_name):
        print(f"This was not found in the {database_name} database. Please try again. ")

    def IDs_dont_match(self, value_1, value_2):
        print(f"{value_1} doesn't match with {value_2}. Please try again. ")

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

    def back_to_menu(self):
        print("Going back to main menu... ")



