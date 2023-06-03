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
        '''Takes in the table name and a list of values (in order)
        and enters them into the database.
        - WARNING: make sure you put the values in the correct order
        that the columns are in!!!
        - NOTE: skips the first column because it's an incrementing ID column.'''
    
        num_values = len(value_list)

        if num_values == 0:
            return

        query = f"INSERT INTO {table_name} VALUES (NULL,"

        for i in range(num_values):
            query += "?,"

        query = query.rstrip(",") + ")"

        self._cur.execute(query, value_list)

        self._con.commit()

    def get_id_by_value(self, table_name, value_column_name, value):
        '''Takes in a value and returns the ID corresponding to that value in a table'''

        query = f"SELECT ID FROM {table_name} WHERE {value_column_name} = ?"
        self._cur.execute(query, (value,))
        result = self._cur.fetchone()

        if result:
            return result[0]
        else:
            return None   

    def get_value_by_ID(self, table_name, column_name, ID):
        '''takes in ID and returns the corresponding value in the column you choose.
        NOTE: only returns the first one with that ID. (assuming unique ID's.)'''

        query = f'SELECT {column_name} FROM {table_name} WHERE ID = ?'
        self._cur.execute(query, (ID,))
        result = self._cur.fetchone() 

        if result:
            return result[0]
        else:
            return None
        
    def get_all_from_column(self, table_name, column_name):
        '''returns a list with all the values in a column'''
        self._cur.execute(f'SELECT {column_name} FROM {table_name}')
        rows = self._cur.fetchall()

        return [row[0] for row in rows]

    def get_all_by_ID(self, table_name, column_name, ID_column_name, ID):
        '''returns a list of values with a specific ID'''
        query = f'SELECT {column_name} FROM {table_name} WHERE {ID_column_name} = ?'
        self._cur.execute(query, (ID,))
        rows = self._cur.fetchall()

        return [row[0] for row in rows]
    
    def get_one_value_by_another(self, table_name, value1_column, value1, value2_column):
        '''takes in one value and the column name of the desired value,
        and returns the value in the desired column on the same row as value1'''

        query = f'SELECT {value2_column} FROM {table_name} WHERE {value1_column} = ?'
        self._cur.execute(query, (value1,))
        result = self._cur.fetchone() 

        if result:
            return result[0]
        else:
            return None
        

    def modify_value(self, table_name, column_name, old_value, new_value):
        '''Takes in an old value and a new value. Finds the old value in the 
        table and changes it to the new value.'''

        query = f'UPDATE {table_name} SET {column_name} = ? WHERE {column_name} = ?'
        self._cur.execute(query, (new_value, old_value))

        self._con.commit()


    def delete_value(self, table_name, column_name, value):
        '''Takes in a value and deletes the row containing that value from the table.'''
        
        query = f'DELETE FROM {table_name} WHERE {column_name} = ?'
        self._cur.execute(query, (value,))

    def check_table_existence(self, table_name):
        '''returns true if table exists and false if not'''
        try:
            self._cur.execute(f"SELECT * FROM {table_name}")
            return True
        except _sqlite3.OperationalError:
            return False
        
    def get_all_values(self, table_name):
        '''returns a list of all the values in a table'''

        query = f'SELECT * FROM {table_name}'
        self._cur.execute(query)

        return self._cur.fetchall()
    
    def get_all_values_in_column(self, table_name, column_name):
        '''returns a list of all the values in a specific column of a table'''

        query = f'SELECT {column_name} FROM {table_name}'
        self._cur.execute(query)

        tuples = self._cur.fetchall()
        return [value[0] for value in tuples]
    
    def get_value_column_name_gradschoolDB(self, table_name):
        '''NOTE: THIS IS SPECIFIC TO THE GRADSCHOOL DATABASE
        takes in the table name and returns the column where
        the value is, (as opposed to the ID columns)'''

        column_names = {
            "career_path": "Career_path",
            "program": "Program",
            "school": "School"
        }

        return column_names.get(table_name)





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