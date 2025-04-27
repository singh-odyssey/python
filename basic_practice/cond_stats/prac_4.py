# Write a program to find if the user input string contains less than 10 characters.

user_in = input("Enter your text -> ")
if len(user_in) < 10:
    print("The input contains less than 10 characters.")
else:
    print("The input contains 10 or more characters.")