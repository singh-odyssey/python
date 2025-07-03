# armstrong number .
num=int(input("enter your number - > " ))
length=len(str(num))
temp = num
sum = 0

while temp>0:
    digit = temp%10
    sum += digit**length
    temp = temp//10

if sum==num:
    print("it is an armstrong number ")
else:
    print("it is not an armstrong number")