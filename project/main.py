# my own classes:
import db_accessor
import ui

def main():
    # initialize the classes we will be using
    _ui = ui.UI()
    database = db_accessor.db_accessor()
    
    x = True
    while x:
        _ui.clear_screen()

        # ask user what they want to do:

        # options: 
        # adding stuff:
        # - Add a career path
        # - Add a school
        # - Add a program
        # accessing stuff
        # - See what schools I have applied for
        # - search database by category
        # changing stuff
        # - mark a program as applied
        # - favorite a program
        # - un-favorite a program
        # other
        # - Quit
        
        user_input = _ui.display_menu()
        print(user_input)
        input()

        # allowing user to quit
        if user_input == "quit":
            x = False

        if user_input == "add school":
            # get the school name:
            school_name = _ui.get_school_name()

            # get the school city:
            school_city = _ui.get_school_city()

            # (check if the city is in the city database)

            # get the school state:
            school_state = _ui.get_school_state()

            # (check if the state is in the state database)
            
            # confirm addition to database:
            if _ui.confirm_add_to_database(f"{school_name}: {school_city}, {school_state}", "(enter database here)"):
                # (add it to the database)
                _ui.adding_to_database()
            else:
                _ui.back_to_menu()
             



if __name__ == "__main__":
    main()