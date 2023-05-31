# my own classes:
import db_accessor
import ui

def main():
    # initialize the classes we will be using
    user_interface = ui.UI()
    database = db_accessor.db_accessor()
    
    print("is it working?")

if __name__ == "__main__":
    main()