# convert celcius to farenheit

def celcius():
    f=int(input("Enter farenheit ->  "))
    c =((f-32)*5)/9
    print(f"Temperature in Celcius is : {c}")

def farenheit():
    c=int(input("Enter the celcius -> "))
    f = (c * 9/5) + 32
    print(f"Temperature in Fahrenheit: {f}")

user_input=input("Enter C to covert in celcius or F to convert in farenheit -> ")

if user_input.lower() == 'c' or user_input=='C':
    celcius()
else:
    farenheit()
