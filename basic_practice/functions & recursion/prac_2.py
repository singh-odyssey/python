# prog to find greatest of 3 number using function

num1 =int(input("Enter the first number -> "))
num2 =int(input("Enter the first number -> "))
num3 =int(input("Enter the first number -> "))

def greatest(num1 ,num2 , num3):
    if num1>num2 and num1>num3 :
        print(f"num1 is greatest which is {num1}")
    elif num2>num1 and num2>num3:
        print(f"num2 is greatest which is {num2}")
    else:
        print(f"num3 is greatest which is {num3}")
     

greatest(num1,num2,num3)
