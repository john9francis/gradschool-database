# Overview

This program "grad school database" is designed to help someone organize grad schools they want to apply for. To use, simply follow the steps on the menu to add a grad school, search for grad schools in the database, or mark a grad school as applied. You can also search for grad schools by location, program, or tuition cost. 

I wrote this software for two reasons. First, I wanted a database containing all the grad schools I have applied for or what to apply for. Second, I created this project to teach myself SQL. If you are a beginner to SQL, my code should be easy to understand because I am a beginner myself.

[//]: # (Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.)

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using the SQL relational database, specifically Python's built in "sqlite3."

The program has a easy-to-use menu, but if you want to use the database itself, here is it's structure:

### gradSchools.db structure:
School table: 

| ID | School | State ID | City ID |
|----|--------|----------|---------|

Career path table:

| ID | Career path (computer science, physics, etc) |
|---|---|

Program table:

| ID | School ID | Career path ID | Program | Credits required | tuition cost | applied? | favorite? |
|---|---|---|---|---|---|---|---|

US cities and states table:

[Borrowed from kelvins US cities database](#useful-websites)

# Development Environment

I coded this project in Python using Visual Studio Code. I used the sqlite3 library which is an included library, so no need to install any different libraries. 

# License

This software was created under the [MIT license](LICENSE).

# Useful Websites

- [SQLite3 download](https://www.sqlite.org/download.html)
- [Setting up Python virtual environment](https://www.youtube.com/watch?v=KxvKCSwlUv8)
- [Basic overview of SQL (video)](https://www.youtube.com/watch?v=h8IWmmxIyS0)
- [Useful sqlite3 tutorial (video)](https://www.youtube.com/watch?v=pd-0G0MigUA)
- [SQLite data types](https://www.sqlite.org/datatype3.html)
- [kelvins US cities database](https://github.com/kelvins/US-Cities-Database)

# Future Work

- Item 1
- Item 2
- Item 3
