A file named "users.txt" is given in which usernames, passwords and friend lists are stored in a
certain way. When your program runs, this file will be read, the main menu will be shown and
the user will be asked to enter an option. If an invalid option is entered, the user will be
warned, the main menu will be shown again and another user input will be requested.

Main menu should look like this:

1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Save and exit

➔ If 1 is entered, the user will be asked to enter a username and a password:
◆ If a user is found with the entered name and password the program should
log in the user by keeping the entered user name in the memory.
◆ If the entered user name does not exist or the password and the username do
not match then the program should print out “Wrong password or user name”.
➔ If 2 is entered, the user will be asked to enter a new username and a password:
◆ If the entered username is valid & unique, and the entered password is valid
then the user list should be updated with the new info. The logged in user
should not change after a new user creation.
◆ If the entered username already exists in the user list or it’s not valid the
program should print out “Username not valid”.
◆ If the password is not valid then the program should print out “Password not
valid”
➔ If 3 is entered, depending on the login status:
◆ If a user is logged in, the user will be asked to enter the name of their new
friend.
● If the entered name exists in the user list, the logged in user’s friend
list must be updated with the entered name.
● If the entered name does not exist in the user list, the program should
print out “Friend not found”
◆ If the user is not logged in then the program should print out “You need to log
in first”
➔ If 4 is entered, depending on the login status:
◆ If a user is logged in, the logged in user’s friend list should be printed out
◆ If the user is not logged in then the program should print out “You need to log
in first”
➔ If 5 is entered, then the updated user list in the memory will be saved to the file and then
the program will quit.➔ For all of the options except 5, when the task is completed, the main menu will be shown
again.
Notes:
● Implement a function to validate usernames. Usernames must be unique, should only
contain numbers and english lowercase letters between a-z, should not be empty
strings.
● Implement a function to validate passwords. Password length should be between
4-8, it should contain at least one letter and one number.
● A single line of users.txt file consists of 3 parts which are username, password, and
friend list. Each part is separated by the “;” character.
● You must call a function for each menu option. Your loop for the main menu should
not be longer/more complex than it needs to be.
● This homework will be graded mostly automatically. Be very careful about your
outputs. Example input and output files are given with your homework. You can test
your own code with the given files. For your convenience an example run with the
outputs, and all the print statements are given below.

Example run:

1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Exit
1
Please enter username:
ali
Please enter password:
1234
Logged in
1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Exit
6
Invalid option
1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Exit
4ahmet,ovgu,ayse
1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Exit
5

All print/input statements(some are used more than once):
input("Please enter username:\n")
input("Please enter password:\n")
print("Logged in\n")
print("Wrong password or username\n")
print("Username not valid\n")
print("Password not valid\n")
input("Please enter the name of your new friend:\n")
print("Friend not found\n")
print("You need to log in first\n")
menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4.
Show my friends\n5. Exit\n"
print(menu_text)
print("Invalid option\n")