'''
This class accesses the database and either creates tables or
accesses the info you need.
'''

import _sqlite3

class db_accessor:
    def __init__(self, path):
        # first, connect to a db file.
        self._con = _sqlite3.connect(path)

        # cursor allows us to execute sql commands
        self._cur = self._con.cursor()


    def close_database(self):
        '''close the connection'''
        self._cur.close()
        self._con.close()

    def check_value_existence(self, table_name, column_name, value):
        '''takes in a value and checks if it's in the database'''

        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?"
        self._cur.execute(query,(value,))
        result = self._cur.fetchone()[0]

        if result > 0:
            return True
        else:
            return False

    def check_matching_ID_us_cities(
            self,
            state_code,
            city_value):
        '''takes in a parent value and a child value,
        and checks to see if the parent ID matches the child's parent ID.'''

        # now get the parent's ID
        self._cur.execute(f"""SELECT ID 
                        FROM US_STATES 
                        WHERE STATE_CODE='{state_code}'""")
        parent_ID = self._cur.fetchone()

        # get the child's parent ID
        self._cur.execute(f"""SELECT ID_STATE 
                        FROM US_CITIES
                        WHERE CITY='{city_value}'""")
        
        # go through the state ID's and if one of them matches, return true
        state_IDs = self._cur.fetchall()
        for ID in state_IDs:
            if ID == parent_ID:
                return True
            
        return False
    
    def add_to_database(self, table_name, value_list):
        '''takes in the table name and a list of values (in order)
        and enters them into the database. 
        - WARNING: make sure you put the values in the correct order
        that the columns are in!!!'''
        pass
    


#region DANGER ZONE, READ FUNCTION DESCRIPTIONS

    def create_tables(self):
        '''one time function to create our 3 tables:'''

        # School table
        self._cur.execute('''CREATE TABLE IF NOT EXISTS school
                       (ID integer, School text, Country_ID integer, 
                       State_ID integer, City_ID integer)''')
        # career path table
        self._cur.execute('''CREATE TABLE IF NOT EXISTS career_path
                       (ID integer, Career_Path text)''')
        # program table
        self._cur.execute('''CREATE TABLE IF NOT EXISTS program
                       (ID integer, School_ID integer, Carrer_Path_ID integer, 
                       Program text, Credits_Required integer, tuition_cost real, 
                       applied integer, favorite integer)''')
        
    def add_autoincrement(self):
        '''A one-time function to change the tables to 
        Autoincrementing tables (automatically generate unique ID's)
        - WARNING: make sure you go in and change all the values and stuff
        before running this code!'''

        # program table
        # ID, School_ID, Career_Path_ID, Program

        # Create a new temporary table with the desired structure
        self._cur.execute("""DROP TABLE program""")
        self._cur.execute("""CREATE TABLE program (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            School_ID INTEGER,
                            Career_Path_ID INTEGER,
                            Program text
                        )""")

        self._con.commit()

#endregion