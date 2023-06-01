# my own classes:
import db_accessor
import ui

def main():
    # initialize the classes we will be using
    _ui = ui.UI()
    grad_school_db = db_accessor.db_accessor("project/databases/gradSchools.db")
    us_cities_db = db_accessor.db_accessor("project/databases/us_cities.db")

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

        

        if user_input == "add school":
            # get the school name:
            school_name = _ui.get_school_name()

            valid_city = False
            while not valid_city:
                # get the school city:
                school_city = _ui.get_school_city()

                # (check if the city is in the city database)
                if us_cities_db.check_value_existence("US_CITIES","CITY",school_city):
                    valid_city = True
                else:
                    _ui.not_in_database("US_CITIES")

            

            # (check if the state is in the state database)
            valid_state = False
            while not valid_state:
                # get the school state:
                school_state = _ui.get_school_state()

                # (check if the state is in the state database)
                if us_cities_db.check_value_existence("US_STATES","STATE_CODE",school_state):
                    valid_state = True
                else:
                    _ui.not_in_database("US_STATES")

            # (check if the city exists in the state)
            print(us_cities_db.check_matching_ID(school_state, school_city))
            input()

            # confirm addition to database:
            if _ui.confirm_add_to_database(f"{school_name}: {school_city}, {school_state}", "grad schools"):
                # (add it to the database)
                _ui.adding_to_database()
            else:
                _ui.back_to_menu()

        # allowing user to quit
        if user_input == "quit":
            x = False

    # end of that while loop===

    # don't forget to close those databases
    grad_school_db.close_database()
    us_cities_db.close_database()
             

if __name__ == "__main__":
    main()