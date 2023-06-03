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
                school_city = _ui.get_city()

                # (check if the city is in the city database)
                if us_cities_db.check_value_existence("US_CITIES","CITY",school_city):
                    break
                else:
                    _ui.not_in_database("US_CITIES")

            # (check if the state is in the state database)
            while True:
                # get the school state:
                school_state = _ui.get_state()

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
        '''uses the UI and the grad_school database to add a
        program to the grad school database.'''

        # step 1: get the name of the program
        program_name = _ui.get_program_name()

        # step 2: get the name and ID of the school that offers it
        while True:
            school_choice = _ui.choose_for_program(
                "school", 
                grad_school_db.get_all_from_column("school","School"))
            
            if grad_school_db.check_value_existence("school","School",school_choice):
                break
            else:
                _ui.not_in_database("school")

        # step 3: get the name and ID of the career path it satisfies
        while True:
            career_path_choice = _ui.choose_for_program(
                "career path",
                grad_school_db.get_all_from_column("career_path","Career_path")
            )

            if grad_school_db.check_value_existence("career_path", "Career_path", career_path_choice):
                break
            else:
                _ui.not_in_database("career_path")

        # step 4: add to the program database

        # get the ID's of the school and career path
        school_ID = grad_school_db.get_id_by_value("school","School",school_choice)
        career_path_ID = grad_school_db.get_id_by_value("career_path","Career_path",career_path_choice)

        # add the program to the program database:
        if _ui.confirm_add_to_database(f"{program_name} at {school_choice} to fulfill your {career_path_choice} career","program"):
            _ui.adding_to_database()
            grad_school_db.add_to_database("program", [school_ID, career_path_ID, program_name])

            _ui.user_input_to_continue()
        else:
            _ui.back_to_menu()
            _ui.user_input_to_continue()

    
    def add_career_path():
        '''uses the UI and the grad_school database to add a 
        new career path to the grad school database.'''

        # get the new career path
        career_path = _ui.get_new_career_path()

        # confirm with user
        if _ui.confirm_add_to_database(career_path, "career_path"):
            # add the career path to the database
            _ui.adding_to_database()
            grad_school_db.add_to_database("career_path", [career_path])
            _ui.user_input_to_continue()
        else:
            _ui.back_to_menu()
            _ui.user_input_to_continue()

    
    def search_program_by_state():
        '''asks user to enter a state, and displays all the programs in that state.'''
        
        # get state:
        while True:
            state = _ui.get_state()

            # check that the state is in the database:
            if us_cities_db.check_value_existence("US_STATES","STATE_CODE",state):
                break
            else:
                _ui.bad_input()

        # get the state's ID
        state_ID = us_cities_db.get_id_by_value("US_STATES","STATE_CODE",state)

        # get all the schools in that state:
        school_list = grad_school_db.get_all_by_ID("school","School","State_ID",state_ID)
    
        # get all the programs from that school...
        program_with_school = dict() # key = program, value = school

        # (loop through the schools and get the ID for each)
        for school in school_list:
            school_ID = grad_school_db.get_id_by_value("school","School",school)
            temp_program_list = grad_school_db.get_all_by_ID("program","Program","School_ID",school_ID)

            # add any program from that school into the programs dict
            for p in temp_program_list:
                program_with_school[p] = school

        # tell the user that we're displaying programs in that state
        _ui.displaying_programs_in_category(us_cities_db.get_value_by_ID("US_STATES","STATE_NAME",state_ID))

        # finally, display all the programs
        for program in program_with_school:
            _ui.display_program_with_school(program, program_with_school[program])

        _ui.user_input_to_continue()


    def search_program_by_career():
        '''asks user for their desired career path, and
        displays all the grad programs that fulfill that career path.'''
        '''asks user to enter a state, and displays all the programs in that state.'''
        
        # get all career paths
        career_paths = grad_school_db.get_all_from_column("career_path","Career_path")

        # user inputs career path
        while True:
            career_path = _ui.choose_career_path(career_paths)

            # check if that career_path is in the database:
            if grad_school_db.check_value_existence("career_path","Career_path",career_path):
                break
            else:
                _ui.bad_input()
                _ui.user_input_to_continue()

        # get the career path's ID
        career_ID = grad_school_db.get_id_by_value("career_path","Career_path", career_path)

        # get a list of all the programs with that career_ID
        program_list = grad_school_db.get_all_by_ID("program","Program","Career_Path_ID",career_ID)

        # get all the schools joined with the programs
        program_with_school = dict() # key = program, value = school
        for program in program_list:
            school_ID = grad_school_db.get_one_value_by_another("program","Program",program,"School_ID")
            school = grad_school_db.get_value_by_ID("school", "School", school_ID)
            program_with_school[program] = school

        # tell user we're displaying all the programs in that career path
        _ui.displaying_programs_in_category(career_path)

        # display to the user all the programs with that ID.
        for program in program_with_school:
            _ui.display_program_with_school(program, program_with_school[program])

        _ui.user_input_to_continue()


    def modify_value():
        '''allows the user to modify whatever they want in the database.'''

        # find out what they want to modify.
        while True:
            table_list = ["career_path","program","school"]
            table = _ui.get_table_to_modify(table_list)

            # make sure the table exists:
            if grad_school_db.check_table_existence(table):
                # the table exists
                break
            else:
                _ui.bad_input()

        # get the correct column name
        column_name = grad_school_db.get_value_column_name_gradschoolDB(table)

        while True:
            # get the value to modify
            value = _ui.get_value_to_modify(grad_school_db.get_all_values_in_column(table,str(column_name)))

            # make sure the value is in that certain column:
            if grad_school_db.check_value_existence(table,column_name,value):
                break
            else:
                _ui.bad_input()

        
        # allow user to modify the value
        modified_value = _ui.change_value(value)

        if _ui.confirm_value_change(value, modified_value):
            # go ahead and change the value:
            grad_school_db.modify_value(table, column_name, value, modified_value)
            _ui.success_value_change(value, modified_value)
        else:
            # go back to main menu
            _ui.back_to_menu()
            _ui.user_input_to_continue()

        

    def delete_value():
        pass

    #endregion

    while True:
        _ui.clear_screen()
        
        user_input = _ui.display_menu()

        if user_input == "add school":
            add_school()

        if user_input == "add program":
            add_program()

        if user_input == "add career path":
            add_career_path()

        if user_input == "search program by state":
            search_program_by_state()

        if user_input == "search program by career":
            search_program_by_career()

        if user_input == "modify":
            modify_value()

        if user_input == "quit":
            # get out of the big old while loop
            break

    # don't forget to close those databases
    grad_school_db.close_database()
    us_cities_db.close_database()



if __name__ == "__main__":
    main()