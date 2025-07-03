num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)

# or 

num = int(input("Enter a number: "))
reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)