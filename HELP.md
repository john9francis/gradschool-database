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
