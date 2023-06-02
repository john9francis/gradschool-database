# Tips for using this repo or SQL in general

## Getting a .db file from a .sql file

I had some trouble getting the data from [kelvin's US cities database](link) into a .db file. In his repo, he has a .sql file and instructions to convert it, but since I didn't download SQLite, (I'm only using the python built-in "\_sqlite3"), his help didn't work. So here's what I did to convert his .sql file to a .db file:

First of all, his file looks something like this:

```sql
--
-- Table structure for table `us_states`
--
DROP TABLE IF EXISTS US_STATES;		
CREATE TABLE US_STATES (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	STATE_CODE char(2) NOT NULL,
	STATE_NAME varchar(50) NOT NULL
);

INSERT INTO US_STATES VALUES
(1,'AL','Alabama'),
(2,'AK','Alaska'),
(3,'AZ','Arizona'),
(4,'AR','Arkansas'),
(5,'CA','California'),
(6,'CO','Colorado'),
(7,'CT','Connecticut'),
```

Now, to convert this into a .db file, I used the following code: 

```python
import _sqlite3

# Path to the SQL script file
sql_file = 'us_cities.sql'

# Path to the SQLite database file to be created
db_file = 'us_cities.db'

# Connect to the SQLite database
conn = _sqlite3.connect(db_file)

# Open the SQL script file
with open(sql_file, 'r') as f:
    # Read the SQL script content
    sql_script = f.read()

    # Execute the SQL script using the connection
    conn.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

```

## changing the structure of a table

I ran into an issue where I had already created some tables but then I wanted to change their ID columns to autoincrement (automatically generate unique ID's for each new entry.) The only way to do that is to create a new table with the autoincrement feature, copy all the info from the old table into the new table, and delete the old table. Here's an example of doing that:

```python
import sqlite3

def add_autoincrement():
    conn = sqlite3.connect("your_database.db")
    cursor = conn.cursor()

    # Create a new temporary table with the desired structure
    cursor.execute("""CREATE TABLE TempTable (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Value TEXT
                    )""")
    
    # Copy data from the existing table to the temporary table
    cursor.execute("INSERT INTO TempTable (Value) SELECT Value FROM YourTable")
    
    # Drop the existing table
    cursor.execute("DROP TABLE YourTable")
    
    # Rename the temporary table to the original table name
    cursor.execute("ALTER TABLE TempTable RENAME TO YourTable")

    conn.commit()
    conn.close()

# Usage example
add_autoincrement()

```

