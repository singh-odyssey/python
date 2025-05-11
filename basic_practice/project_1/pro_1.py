# write a prog which generates random number and then ask user to guess the number

import random

random_number = random.randint(1, 100)
user_input = None
count = 0

while user_input != random_number:
    print(" ")
    user_input = int(input("Enter Your number between 1 and 100 -> "))
    count=count+1

    if user_input==random_number:
        print(" ")
        print("Congrats you find the right number")

    elif user_input<random_number:
        print("Larger Number Please")

    else:
        print("Lower Number please")

print(f"Number of attempts are -> {count}")        

# saving the minimum number of attempts in a file to show user it as best score 

with open("score_pro_1.txt", "r+") as file:
    old_file = file.read()
    if old_file == '':
        file.write(str(count))
        new_file = str(count)  
    elif int(old_file) > count:
        with open("score_pro_1.txt", "w") as file:
            file.write(str(count))
        new_file = str(count)
    else:
        new_file = old_file  

print(f"mimimum attempted guess of all time is {new_file}")