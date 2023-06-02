# my own classes:
import db_accessor
import ui

def main():
    # initialize the classes we will be using
    _ui = ui.UI()
    grad_school_db = db_accessor.db_accessor("project/databases/gradSchools.db")
    us_cities_db = db_accessor.db_accessor("project/databases/us_cities.db")

    #region main functions

    def add_school():
        '''Uses the UI and the two databases to add a school to the school database'''

        # get the school name:
        school_name = _ui.get_school_name()
        valid_city_and_state = False
        while not valid_city_and_state:
            while True:
                # get the school city:
                school_city = _ui.get_school_city()

                # (check if the city is in the city database)
                if us_cities_db.check_value_existence("US_CITIES","CITY",school_city):
                    break
                else:
                    _ui.not_in_database("US_CITIES")

            # (check if the state is in the state database)
            while True:
                # get the school state:
                school_state = _ui.get_school_state()

                # (check if the state is in the state database)
                if us_cities_db.check_value_existence("US_STATES","STATE_CODE",school_state):
                    break
                else:
                    _ui.not_in_database("US_STATES")
            
            # (check if the city has the state ID)
            if us_cities_db.check_matching_ID_us_cities(school_state, school_city):
                valid_city_and_state = True
            else:
                _ui.IDs_dont_match(school_city, school_state)

        # confirm addition to database:
        if _ui.confirm_add_to_database(f"{school_name}: {school_city}, {school_state}", "grad schools"):
            # (add it to the database)
            _ui.adding_to_database()
            # step one: find the state_id and the city_id
            state_id = us_cities_db.get_id_by_value("US_STATES", "STATE_CODE", school_state)
            city_id = us_cities_db.get_id_by_value("US_CITIES", "CITY", school_city)
            country_id = 1 # USA
            # step two: put these values in a list with the specific order
            school_value_list = [school_name, country_id, state_id, city_id]
            # step three: add the grad school to the database.
            grad_school_db.add_to_database("school", school_value_list)

            _ui.user_input_to_continue()
        else:
            _ui.back_to_menu()
            _ui.user_input_to_continue()

    
    def add_program():

        pass

    
    def add_career_path():
        '''uses the UI and the grad_school database to add a 
        new career path to the grad school database.'''

        # get the new career path
        career_path = _ui.get_career_path()

        # confirm with user
        if _ui.confirm_add_to_database(career_path, "career_path"):
            # add the career path to the database
            _ui.adding_to_database()
            grad_school_db.add_to_database("career_path", [career_path])
            _ui.user_input_to_continue()
        else:
            _ui.back_to_menu()
            _ui.user_input_to_continue()


    #endregion

    while True:
        _ui.clear_screen()
        
        user_input = _ui.display_menu()

        if user_input == "add school":
            add_school()
        if user_input == "add program":
            #add_program()
            pass
        if user_input == "add career path":
            add_career_path()
        if user_input == "quit":
            # get out of the big old while loop
            break

    # don't forget to close those databases
    grad_school_db.close_database()
    us_cities_db.close_database()



if __name__ == "__main__":
    main()