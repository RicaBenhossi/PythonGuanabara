# Exercise 115 Python (World 03)

## Scope Version 1.0.0

- Create a system that allows user to register name and age of a person and save in a text file.
- System should allow user to:
  1. Register a new user
  2. List all users registered
- System should be modularized

## Tasks

- [ ] If the file to store data doesn't exist, create it.
- [x] Show up a menu with 3 options: 1 - New User; 2 - List Registred Users; 0 - Exit

### Menu 1: New User

- [ ] Ask user to input a new user name (string)
- Name Validations:
  - [ ] Cut out spaces at the begining and at the end
  - [ ] Shouldn't have numbers. It's a name. : Warn about this error
- [ ] Ask User to input the age (integer)
- Age Validations
  - [ ] Type must be an integer: Warn about this error
  - [ ] Must be positive: : Warn about this error
- [ ] Save it in database file
- [ ] Print a message if the insertion was successfully
- [ ] Clean up screen and shows up MENU

### Menu 2: List User

- [ ] Open database file
- [ ] Load all content of the file to a variable and close file
- [ ] Print all data on screen (table like)
- [ ] Shows up MENU

### Menu 0: Exit

- [ ] Print a good bye message
- [ ] Close application
