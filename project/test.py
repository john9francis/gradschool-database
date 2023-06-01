# testing to see what tables are in the us_cities database.
import _sqlite3

conn = _sqlite3.connect('project/databases/us_cities.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    print(table[0])

cursor.close()
conn.close()