# Overview

This program "grad school database" is designed to help someone organize grad schools they want to apply for. It uses a SQL relational database to store the grad programs as well as schools, locations of schools (cities and states) and career paths.

To use, follow the easy-to-use menu (on the console) that gives you options to:
1. Add a new grad school (e.g. university of georgia)
2. Add a new Career Path (e.g. software engineer)
3. Add a new program (e.g. masters in electrical engineering)
4. View all saved programs
5. Search programs by state
6. Search programs by career path
7. Modify something from your database
8. Delete something from your database
9. press q any time to quit

I wrote this software for two reasons. First, I wanted a database containing all the grad schools I have applied for or what to apply for. Second, I created this project to teach myself SQL. If you are a beginner to SQL, my code should be easy to understand because I am a beginner myself. I also created a "help" file with some problems I ran into while creating this project, and solutions to how I solved them. Access it [here.](HELP.md)

[//]: # (Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.)

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using the SQL relational database, specifically Python's built in "sqlite3."

If you want to use the database, here is it's structure:

### gradSchools.db structure:
career_path:
|ID (auto-enumerating integer)|Career_path (text)|
|---|---|

program:
|ID (auto-enumerating integer)|School_ID (integer)|Career_Path_ID (integer)|Program (text)|
|---|---|---|---|

school:
|ID (auto-enumerating integer)|School (text)|Country_ID (integer)|State_ID (integer)|City_ID (integer)|
|---|---|---|---|---|

### us_cities.db structure:

[see kelvins US cities database](https://github.com/kelvins/US-Cities-Database)


# Development Environment

I coded this project in Python using Visual Studio Code. I used the sqlite3 library which is an included library, so no need to install any different libraries. 

# License

This software was created under the [MIT license](LICENSE).

# Useful Websites

Development environment stuff:
- [Setting up Python virtual environment](https://www.youtube.com/watch?v=KxvKCSwlUv8)

Tutorial videos: 
- [Basic overview of SQL](https://www.youtube.com/watch?v=h8IWmmxIyS0)
- [Useful sqlite3 beginner tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA)

Help with learning the syntax of SQLite:
- [SQLite data types](https://www.sqlite.org/datatype3.html)
- [W3Schools SQL syntax (super useful)](https://www.w3schools.com/sql/sql_syntax.asp)

Super nice application to visualize your database  (I highly recommend it):
- [DB browser download](https://sqlitebrowser.org/)

Where I got the database of cities and states:
- [kelvins US cities database](https://github.com/kelvins/US-Cities-Database)

# Future Work

- Add a way to delete schools, programs, or career paths
- Add a method for marking schools applied or not yet applied for
- Add a new table called "more_info" where the user can add extra info about a program like tuition cost, credits required, etc.
