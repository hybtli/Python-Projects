myfile = open('users.txt')
myfile = myfile.read()
myfile_ =  myfile.split("\n")

users_list = []
password_list = []
friends_list = []

for i in myfile_:
    b = i.split(';')
    if b[0] == '' or b[1] == '' or b[2] == '':
        pass
    else:
        users_list.append(b[0])
        password_list.append(b[1])
        friends_list.append(b[2])

con = False

def login(username,password):

    if  username in users_list:
        if users_list.index(username) == password_list.index(password):
            print("Logged in\n")
        else:
            print("Wrong password or username\n")
    else:
        print("Wrong password or username\n")

def createuser(username):

    if username in users_list:
        return  False
    for i in username:
        if not (i.isnumeric() or i.islower()):
            return False
    return True

def createpassword(password):

    if 4 <= len(password) <= 8:
        return True
    for i in password:
        if i.isnumeric():
            return True
        if i.isalpha():
            return True

def newuser():

    username = input("Please enter username:\n")
    password = input("Please enter password:\n")

    if createuser(username):
        if createpassword(password):
            users_list.append(username)
            password_list.append(password)
            friends_list.append('')
        else:
            print("Password not valid\n")
    else:
        print("Username not valid\n")

def addfriend(username):

    friend = input("Please enter the name of your new friend:\n")
    if friend in users_list:
        if friends_list[users_list.index(username)] == '':
            friends_list[users_list.index(username)] += (friend)
        else:
            friends_list[users_list.index(username)] += (','+friend)
        return
    else:
        print("Friend not found\n")
        return

def showfriends(username):

    print(friends_list[users_list.index(username)])
    return

def exit():

    myfile = open('users.txt', 'w')
    string = ''
    for ch in users_list:
        string += ch + ';' + password_list[users_list.index(ch)] + ';' + friends_list[users_list.index(ch)] + "\n"
    myfile.write(string)
    myfile.close()
    quit()

while True:
    choice = input("1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n")

    if choice == "1":
        username = input("Please enter username:\n")
        password = input("Please enter password:\n")
        login(username,password)
        con = True
    elif choice == "2":
        newuser()
    elif choice == "3":
        if con == False:
            print("You need to log in first\n")
        else:
            addfriend(username)
    elif choice == "4":
        if con == False:
            print("You need to log in first\n")
        else:
            showfriends(username)
    elif choice == "5":
        exit()
    else:
        print("Invalid option\n")