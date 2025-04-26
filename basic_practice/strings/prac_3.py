#detect double space in a string on user input 

user_input = input("Enter a string: ")
detect=user_input.find("  ")

if detect != -1:
    print("Double space detected at index:", detect)
else:
    print("No double spaces detected.")