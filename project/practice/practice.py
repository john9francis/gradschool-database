import _sqlite3

# first, connect to a db file.
con = _sqlite3.connect('project/practice/example.db')

# cursor allows us to execute sql commands
cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE stocks
#               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2023-05-27','BUY','AAPL',10,121.23)")

# query the value we want
cur.execute("SELECT * FROM stocks WHERE trans='BUY'")

# get that value we queried
print(cur.fetchall())

# delete the stocks table:
# cur.execute("DROP TABLE stocks")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()




# summary: 
# cursor does all the actions.
# some things we can do with the cursor:
# CREATE TABLE
# INSERT INTO
# SELECT * FROM
# fetchone(), fetchmany(int), fetchall()
# commit()
# close()
