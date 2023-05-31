import _sqlite3

# first, connect to a db file.
con = _sqlite3.connect('project/gradSchools.db')

# cursor allows us to execute sql commands
cur = con.cursor()



# save changes and close the connection
con.commit()
con.close()