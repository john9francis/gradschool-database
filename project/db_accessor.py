'''
This class accesses the database and either creates tables or
accesses the info you need.
'''

import _sqlite3

class db_accessor:
    def __init__(self) -> None:
        # first, connect to a db file.
        self._con = _sqlite3.connect('project/gradSchools.db')

        # cursor allows us to execute sql commands
        self._cur = self._con.cursor()

    def close_database(self):
        # save changes and close the connection
        self._con.close()
