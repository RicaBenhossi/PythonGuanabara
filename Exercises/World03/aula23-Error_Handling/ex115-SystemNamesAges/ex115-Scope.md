# Exercise 115 Python (World 03)

## Scope Version 1.0.0

- Create a system that allows user to register name and age of a person and save in a text file.
- System should allow user to:
  1. Register a new user
  2. List all users registered
- System should be modularized

## Tasks

- [x] If the file to store data doesn't exist, create it.
- [x] Show up a menu with 3 options: 1 - New User; 2 - List Registred Users; 0 - Exit
- [x] Ask for a menu option (validate if menu exist)

### Menu 1: New User

- [x] Ask user to input a new user name (string)
- Name Validations:
  - [x] Cut out spaces at the begining and at the end
  - [x] Shouldn't have numbers. Warn about this error
  - [x] Must not have special characters (except '-'). Warn about this error.
- [x] Ask User to input the age (integer)
- Age Validations
  - [x] Type must be an integer: Warn about this error
  - [X] Must be positive: : Warn about this error
- [x] Save it in database file
- [x] Print a message if the insertion was successfully
- [x] Clean up screen and shows up MENU

### Menu 2: List User

- [x] Open database file
- [x] Load all content of the file to a variable and close file
- [x] Print all data on screen (table like)
- [x] Shows up MENU

### Menu 0: Exit

- [x] Print a good bye message
- [x] Close application
