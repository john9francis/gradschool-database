# Overview

This program "grad school database" is designed to help someone organize grad schools they want to apply for. To use, simply follow the steps on the menu to add a grad school, search for grad schools in the database, or mark a grad school as applied. You can also search for grad schools by location, program, or tuition cost. 

I wrote this software for two reasons. First, I wanted a database containing all the grad schools I have applied for or what to apply for. Second, I created this project to teach myself SQL. If you are a beginner to SQL, my code should be easy to understand because I am a beginner myself.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

{Describe the relational database you are using.}
I am using the SQL relational database, specifically Python's built in "sqlite3."

The program has a easy-to-use menu, but if you want to use the database itself, here is it's structure:

### gradSchools.db structure:
Main table: 

| ID | School | Country ID | State ID | City ID |
|----|--------|---------|

Country table:
| ID | Country |
|---|---|

US cities table:
| School ID | City | State |
|---|---|---|

Category table:

| ID | Category (computer science, physics, etc) |
|---|---|

Program child table:

| ID | School ID | Category ID | Program | Credits required | tuition cost |
|---|---|---|---|---|---|

# Development Environment

The code for this project will primarily be written in Python using Visual Studio Code. The libraries I will be using are found in the requirements.txt file. To run this project on your own machine, clone the repository and then you can run:
```
pip install -r requirements.txt
```
and it will automatically install all the libraries that I have used. 

# Useful Websites

- [Setting up Python virtual environment](https://www.youtube.com/watch?v=KxvKCSwlUv8)
- [Basic overview of SQL](https://www.youtube.com/watch?v=h8IWmmxIyS0)
- [Useful sqlite3 tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA)
- [Database of US cities and states](https://github.com/kelvins/US-Cities-Database)

# Future Work

- Item 1
- Item 2
- Item 3
