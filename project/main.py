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
        
        user_input = _ui.get_input()
        print(user_input)

        # allowing user to quit
        if user_input == "quit":
            x = False


if __name__ == "__main__":
    main()