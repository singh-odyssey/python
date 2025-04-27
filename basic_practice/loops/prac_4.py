#prog to find a number is prime or not 
num =int(input("Enter your number -> "))

for i in range(2, num // 2+1):
    if num%i==0:
        print("Number is not prime")
        break
else:
        print("Number is  prime ")  
    