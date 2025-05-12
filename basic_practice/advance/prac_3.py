# use comprehension list and print table of user input 
user_input=int(input("Enter the number -> "))

table = [user_input * i for i in range(1, 11)]
print(f"Table of {user_input}: {table}")