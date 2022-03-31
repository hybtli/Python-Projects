myfile = open("TaskList.txt")
# In first three lines I am opening the text file and reading file by spliting \n
myfile = myfile.read()
myfile_ = myfile.split("\n")

TaskList = []
Hall = []
hp_hero = 3000
hp_pegasus = 550
foot = 20
pegasus = 50
hour_pegasus = 0
hour_foot = 0
hour = 0
damage_foot = 0
damage_pegasus = 0
con = False


# Line 20-23 I append all data to TaskList consecutively
for i in myfile_:
    b = i.split(",")
    TaskList.append(b)


# Recursive Function for removing Task
def remove_task(task_list, Task):
    if task_list[0][0] == Task:
        return task_list[1:]

    return task_list[:1] + remove_task(task_list[1:], Task)


def print_remaining_tasks(TaskList):  # Recursive Function for Remaning Task
    if TaskList == []:
        return ''

    else:
        sub = TaskList[0]
        # It will be misundertanding for you that (12-(len(sub[3])+1))*' ' why program print empty string like that.Because I count in table that How many there is empty string if there is no word after counting I write like that and each section count is different. Also I used this in Hall of Fame function Line 48
        print('| ' + sub[0] + (12-(len(sub[0])+1))*' ' + '| ' + sub[1] + (18-(len(sub[1])+1))*' ' +
              '| ' + sub[2] + (20-(len(sub[2])+1))*' ' + '| ' + sub[3] + (12-(len(sub[3])+1))*' ' + '|')
        print(66 * "-")

        return print_remaining_tasks(TaskList[1:])


def Hall_of_Fame(Hall):                # Recursive Function for Hall of Fame Table

    if Hall == []:
        return ''

    else:
        sub_hall = Hall[0]
        print('| ' + str(sub_hall[0]) + (10-(len(sub_hall[0]))-1)*' ' + '| ' +
              str(sub_hall[1]) + ' hour' + (13-(len(sub_hall[1]))-6)*' ' + '|')
        print('--------------------------')

        return Hall_of_Fame(Hall[1:])


print("Welcome to Hero’s 5 Labors!")
print("Remaining HP for Hero : ", hp_hero)
print("Remaining HP for Pegasus : ", hp_pegasus)
print("Here are the tasks left that hero needs to complete:")
print(66 * "-")

while TaskList != []:               # This while loop will be work until TaskList is empty and in some little condition loop will be breaked and you will the reason in code

    print("| TaskName   | ByFootDistance   | ByPegasusDistance  |  HPNeeded |")
    print(66 * "-")
    print(print_remaining_tasks(TaskList))

    while True:
        # In this while we will ask from the user task input until task name in TaskList and by using .capitalize() I terminate all task input's first letter to capital letter
        task = input("Where should Hero go next? ").capitalize()
        if task not in list(zip(*TaskList))[0]:
            print("Invalid input")
        else:
            break

    while True:
        # In the beginning of this while loop I ask to user to enter travel type and again .capitialize() for the same reason
        type1 = input("How do you want to travel?(Foot/Pegasus)").capitalize()

        # Between Line 86-113 I am calculating all math issue in here before the validatio part. The reason is that we can detect earlier that in some task hp won't be enough and maybe it willl be game over.To detect this calculation was done firstly.
        for sublist in TaskList:
            if task in sublist:
                # Calculation HP and hour when hero choose to go with pegasus
                if type1 == "Pegasus":
                    hp_hero = hp_hero - \
                        int(TaskList[TaskList.index(sublist)][3])
                    damage_pegasus = (
                        int(TaskList[TaskList.index(sublist)][2]) / pegasus
                    ) * 15
                    hp_pegasus = hp_pegasus - damage_pegasus
                    hour_pegasus += int(
                        TaskList[TaskList.index(sublist)][2]) / pegasus
                    break
                # Calculation HP and hour when hero choose to go by foot
                elif type1 == "Foot":
                    if task == 'Task1' or task == 'Task2':
                        break

                    damage_foot = (int(TaskList[TaskList.index(sublist)][3])) + (
                        (int(TaskList[TaskList.index(sublist)][1]) / foot) * 10
                    )
                    hp_hero = hp_hero - damage_foot
                    hour_foot += int(TaskList[TaskList.index(sublist)]
                                     [1]) / foot
                    break

        hour = hour_foot + hour_pegasus

        # Between Line 115-150 there are conditions for when program should print Invalid or There is no enough HP for Hero/Pegasus.
        if type1 not in ["Foot", "Pegasus"]:
            print("Invalid input")
        elif (hp_hero + damage_foot < damage_foot and hp_pegasus + damage_pegasus < damage_pegasus) or (            # In this condition used for if there is no HP for hero or pegasus to travel or there is no HP for pegasus and chosen Task is Task1 or Task2(because in these tasks Hero can not go by foot , even there is a enough HP),then print 'Game Over'
                hp_pegasus + damage_pegasus < damage_pegasus and (task == 'Task1' or task == 'Task2')):
            print('Game Over')
            # I changed condition named 'con' from False to True due to if in main While Loop con = True , then it is Game Over and loop will be break
            con = True
            if type1 == 'Foot':
                # Actually for this data there is no need this code from line 123-131, however if you want to print HP or Time after Game Over then there will be miscalculation and that is why this code between these lines is used for
                hp_hero += damage_foot
                hour -= int(TaskList[TaskList.index(sublist)][1]) / foot
            elif type1 == 'Pegasus':
                hp_pegasus += damage_pegasus
                hp_hero += int(TaskList[TaskList.index(sublist)][3])
                hour -= int(TaskList[TaskList.index(sublist)][2]) / pegasus
            break
        # There is a condition that when needed HP is not enough then program should print there is no enough HP and calculation for backed up decreased HP and increased time due to there is not any travel
        elif hp_hero + damage_foot < damage_foot and type1 == "Foot":
            print("Hero does not have enough HP.")
            hp_hero += damage_foot
            hour_foot -= int(TaskList[TaskList.index(sublist)][1]) / foot
        # And same thing for Pegasus travel type, there is a condition that when needed HP is not enough then program should print there is no enough HP and calculation for backed up decreased HP and increased time due to there is not any travel
        elif hp_pegasus + damage_pegasus < damage_pegasus and type1 == "Pegasus":
            print("Pegasus does not have enough HP.")
            hp_pegasus += damage_pegasus
            hp_hero += int(TaskList[TaskList.index(sublist)][3])
            hour_pegasus -= int(TaskList[TaskList.index(sublist)][2]) / pegasus
        # Condition between Line 143-150 is speacial condition when task input is Task1/Task2 and travel type input is Foot then program should print You cannot go by Foot due to it is impossible as a given data
        elif task == "Task1" or task == "Task2":
            if type1 == "Foot":
                print("You cannot go there by foot.")
            else:
                break
        else:
            break

    # As I said , this condition is for when con named 'con'  condition equal to then break in main loop and Game will be end, because player lost game
    if con == True:
        break

    # Printing data about time remaining HP for Hero and Pegasus between 156-160
    print("Hero defeated the monster")
    print("Time Passed : ", int(hour), "hour\n")
    print("Remaining HP for Hero : ", int(hp_hero))
    print("Remaining HP for Pegasus : ", int(hp_pegasus), "\n")

    while True:
        # And in this loop same thing will happen Line between 162-226 but this for travel type which user will enter travel type for how to return to home
        type2 = input("How do you want to travel?(Foot/Pegasus)").capitalize()

        # Between Line 166-188 I am calculating all math issue in here before the validatio part. The reason is that we can detect earlier that in some task hp won't be enough and maybe it willl be game over.To detect this calculation was done firstly.
        for sublist in TaskList:
            if task in sublist:
                # Calculation HP and hour when hero choose to go with pegasus
                if type2 == "Pegasus":
                    damage_pegasus = (
                        int(TaskList[TaskList.index(sublist)][2]) / pegasus
                    ) * 15
                    hp_pegasus = hp_pegasus - damage_pegasus
                    hour_pegasus += int(
                        TaskList[TaskList.index(sublist)][2]) / pegasus
                    break
                # Calculation HP and hour when hero choose to go by foot
                elif type2 == "Foot":
                    if task == 'Task1' or task == 'Task2':
                        break
                    damage_foot = (
                        int(TaskList[TaskList.index(sublist)][1]) / foot) * 10
                    hp_hero = hp_hero - damage_foot
                    hour_foot += int(TaskList[TaskList.index(sublist)]
                                     [1]) / foot
                    break
        hour = hour_foot + hour_pegasus

        # Between Line 190-226 there are conditions for when program should print Invalid or There is no enough HP for Hero/Pegasus.
        if type2 not in ["Foot", "Pegasus"]:
            print("Invalid input")
        elif (hp_hero + damage_foot < damage_foot and hp_pegasus + damage_pegasus < damage_pegasus) or (            # In this condition used for if there is no HP for hero or pegasus to travel or there is no HP for pegasus and chosen Task is Task1 or Task2(because in these tasks Hero can not go by foot , even there is a enough HP),then print 'Game Over'
                hp_pegasus + damage_pegasus < damage_pegasus and (task == 'Task1' or task == 'Task2')):
            print('Game Over')
            # I changed condition named 'con' from False to True due to if in main While Loop con = True , then it is Game Over and loop will be break
            con = True
            if type2 == 'Foot':
                # Actually for this data there is no need this code from line 198-206, however if you want to print HP or Time after Game Over then there will be miscalculation and that is why this code between these lines is used for
                hp_hero += damage_foot
                hour -= int(TaskList[TaskList.index(sublist)][1]) / foot
            elif type2 == 'Pegasus':
                hp_pegasus += damage_pegasus
                hp_hero += int(TaskList[TaskList.index(sublist)][3])
                hour -= int(TaskList[TaskList.index(sublist)][2]) / pegasus
            break
        # There is a condition that when needed HP is not enough then program should print there is no enough HP and calculation for backed up decreased HP and increased time due to there is not any travel
        elif hp_hero + damage_foot < damage_foot and type2 == "Foot":
            print("Hero does not have enough HP.")
            hp_hero += damage_foot
            hour_foot -= int(TaskList[TaskList.index(sublist)][1]) / foot

        # And same thing for Pegasus travel type, # There is a condition that when needed HP is not enough then program should print there is no enough HP and calculation for backed up decreased HP and increased time due to there is not any travel
        elif hp_pegasus + damage_pegasus < damage_pegasus and type2 == "Pegasus":
            print("Pegasus does not have enough HP.")
            hp_pegasus += damage_pegasus
            hour_pegasus -= int(TaskList[TaskList.index(sublist)][2]) / pegasus

        # Condition between Line 219-226 is speacial condition when task input is Task1/Task2 and travel type input is Foot then program should print You cannot go by Foot due to it is impossible as a given data
        elif task == "Task1" or task == "Task2":
            if type2 == "Foot":
                print("You cannot go there by foot.")
            else:
                break
        else:
            break

    # As I said , this condition is for when con named 'con'  condition equal to then break in main loop and Game will be end, because player lost game
    if con == True:
        break

    print("Hero arrived home.")
    print("Time Passed : ", int(hour), "hour\n")

    # Now I am calling remove_task function to remove a task which is done
    TaskList = remove_task(TaskList, task)

    # There is a conditon between 238-244, if TaskList is empty , then all Task is done and that is why program should print Congratulations message or print  data about time remaining HP for Hero and Pegasus and it measn that there is a still tasks which is not done yet
    if TaskList == []:
        print('Congratulations, you have completed the task.')
    else:
        print("Remaining HP for Hero : ", int(hp_hero))
        print("Remaining HP for Pegasus : ", int(hp_pegasus), "\n")
        print("Here are the tasks left that hero needs to complete:")

# Here I write this condition for excution code Line between 251-279 should be when all tasks is done
if TaskList == []:

    # Taking name as input to print for printing owner of score
    name = input('What is your name : ').capitalize()
    # Line between 251-259 I opened new text named Hall_of_Fame and append Name and Hour to text file
    f = open("Hall_of_Fame.txt", "a+")
    f.write(name)
    f.write(',')
    f.write(str(int(hour)))
    f.write(',')
    f.write("\n")
    f.close()
    f = open("Hall_of_Fame.txt", 'r')
    # I opened new text file and append Names and Hours to suitable lists
    for y in f:
        z = y.split(',')
        Hall.append(z)

    print('Hall Of Fame')
    print('--------------------------')
    print('| Name     | Finish Time |')
    print('--------------------------')

    # Function Line 270-273 is for sorting Nested List for Hall of Fame
    def Sorted(Hall):

        return (sorted(Hall, key=lambda x: int(x[1])))

    Hall = Sorted(Hall)
    Hall = Hall[:3]

    # I am calling here Hall_of_Fame function
    print(Hall_of_Fame(Hall))