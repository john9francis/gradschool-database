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

    def create_tables(self):
        '''one time function to create our 3 tables:'''

        # School table
        self._cur.execute('''CREATE TABLE school
                       (ID integer, School text, Country_ID integer, 
                       State_ID integer, City_ID integer)''')
        # career path table
        self._cur.execute('''CREATE TABLE career_path
                       (ID integer, Career_Path text)''')
        # program table
        self._cur.execute('''CREATE TABLE program
                       (ID integer, School_ID integer, Carrer_Path_ID integer, 
                       Program text, Credits_Required integer, tuition_cost real, 
                       applied integer, favorite integer)''')
        
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

    
