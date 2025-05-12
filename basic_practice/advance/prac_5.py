# store the problem 3 table in a file table.txt

# use comprehension list and print table of user input 
user_input=int(input("Enter the number -> "))

table = [user_input * i for i in range(1, 11)]
with open("table.txt", "a") as file:
    file.write(str(table)+ "\n")
    print("Table saved successfully")

with open("table.txt", "r") as file:
    print(file.read())