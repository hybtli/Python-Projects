In the given TaskList.txt, you can find each task’s distance from his home by foot,by pegasus and the needed HP to kill the monster of the task. TaskList.txt is structured as shown below:
TaskName DistanceByFoot DistanceByPegasus HPToKill
Task1          -1              400           50
Task2          -1              500          100
Task3         600              500           75
Task4        1000              500           50
Task5         900              700           80

You have to read TaskList.txt, and create a nested list named task_list that has each task as a list:
task_list = [[Task1,-1,400,50],[Task2,-1,500,100]....]
As you can see from the TaskList file, if there is no route to go to the given task by foot, the distance is given as -1. Therefore, you have to use Pegasus in order to reach these destinations.In the beginning of the game, the hero has 3000HP, while the pegasus has 550HP.The hero can walk at the speed of 20km/hour. The pegasus can fly at the speed of 50km/hour. For each hour of the journey, the hero loses 10HP, while the pegasus loses 15HP.At the end of each task, the hero must return to his home and continue from there.
After completing each task, the program should remove that task from the task list.At each turn, the program should display the remaining tasks and their distances from the hero’s home, and ask for the hero’s next move.
★ You should write remove_task(task_list) and print_remaining_tasks(task_list) in a recursive manner.
The program finishes when there is no task left (“Congratulations, you have completed the task.” message is printed), or the HP of the hero is not enough to kill the monster of the task or the HP of the hero and pegasus is not enough to travel to the given destination (“Game Over” is
printed). If the user succeeds the game, you have to ask his/her name and save the user’s name with the time the
game took to finish. Also, you have to show the Hall of Fame at the end of each successful game which shows the best 3 results so far.

An example scenario for the game world (user inputs are given in bold):
Welcome to Hero’s 5 Labors!
Remaining HP for Hero : 3000
Remaining HP for Pegasus: 550
Here are the tasks left that hero needs to complete:
--------------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
--------------------------------------------------------
| Task1 | -1 km | 400 km | 50 |
| Task2 | -1 km | 500 km | 100 |
| Task3 | 600 km | 500 km | 75 |
| Task4 | 1000 km | 500 km | 50 |
| Task5 | 900 km | 700 km | 80 |
--------------------------------------------------------
Where should Hero go next? Task1
How do you want to travel?(Foot/Pegasus)foot
You cannot go there by foot.
How do you want to travel?(Foot/Pegasus)pegasus
Hero defeated the monster.
Time passed : 8 hour
Remaining HP for Hero : 2950
Remaining HP for Pegasus: 430
How do you want to go home?(Foot/Pegasus)Pega
Invalid input
How do you want to go home?(Foot/Pegasus)Pegasus
Hero arrived home.
Time passed : 16 hour
Remaining HP for Hero : 2950
Remaining HP for Pegasus: 310
Here are the tasks left that hero needs to complete:
--------------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
--------------------------------------------------------
| Task2 | -1 km | 500 km | 100 |
| Task3 | 600 km | 500 km | 75 |
| Task4 | 1000 km | 500 km | 50 |
| Task5 | 900 km | 700 km | 80 |
--------------------------------------------------------
Where should Hero go next? Task2
How do you want to travel?(Foot/Pegasus)foot
You cannot go there by foot.
How do you want to travel?(Foot/Pegasus)pegasus
Hero defeated the monster.
Time passed : 26 hour
Remaining HP for Hero : 2850Remaining HP for Pegasus: 160
How do you want to go home?(Foot/Pegasus)foot
You cannot go there by foot.
How do you want to go home?(Foot/Pegasus)pegasus
Hero arrived home.
Time passed : 36 hour
Remaining HP for Hero : 2850
Remaining HP for Pegasus: 10
Here are the tasks left that hero needs to complete:
--------------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
--------------------------------------------------------
| Task3 | 600 km | 500 km | 75 |
| Task4 | 1000 km | 500 km | 50 |
| Task5 | 900 km | 700 km | 80 |
--------------------------------------------------------
Where should Hero go next? Task3
How do you want to travel?(Foot/Pegasus)pegasus
Pegasus does not have enough HP.
How do you want to travel?(Foot/Pegasus)foot
Hero defeated the monster.
Time passed : 66 hour
Remaining HP for Hero : 2475
Remaining HP for Pegasus: 10
How do you want to go home?(Foot/Pegasus)foot
Hero arrived home.
Time passed : 96 hour
Remaining HP for Hero : 2175
Remaining HP for Pegasus: 10
Here are the tasks left that hero needs to complete:
--------------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
--------------------------------------------------------
| Task4 | 1000 km | 500 km | 50 |
| Task5 | 900 km | 700 km | 80 |
--------------------------------------------------------
Where should Hero go next? Task5
How do you want to travel?(Foot/Pegasus)pegasus
Pegasus does not have enough HP.
How do you want to travel?(Foot/Pegasus)foot
Hero defeated the monster.
Time passed : 141 hour
Remaining HP for Hero : 1645
Remaining HP for Pegasus: 10
How do you want to go home?(Foot/Pegasus)foot
Hero arrived home.
Time passed : 186 hour
Remaining HP for Hero : 1195
Remaining HP for Pegasus: 10
Here are the tasks left that hero needs to complete:
--------------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
--------------------------------------------------------
| Task4 | 1000 km | 500 km | 50 |
--------------------------------------------------------
Where should Hero go next? Task1
Invalid input
Where should Hero go next? Task4
How do you want to travel?(Foot/Pegasus)foot
Hero defeated the monster.
Time passed : 236 hour
Remaining HP for Hero : 645
Remaining HP for Pegasus: 10
How do you want to go home?(Foot/Pegasus)foot
Hero arrived home.
Time passed : 286 hour
Congratulations, you have completed the task.
What is your name : XXXX
Hall Of Fame
--------------------------
| Name | Finish Time |
--------------------------
| XXXX | 286 hour |
-------------------------
