#calculate factorial of a given number 
num=int(input("Enter your number -> "))
start=1
for value in range(1,num+1):
    start=start*value
print(f"Your factorial is -> {start}")