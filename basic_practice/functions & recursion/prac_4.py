# write recursive function to print sum of n natural number 

num=int(input("Enter your number -> "))

def sum(num):
    if num==1:
        return 1
    return num + sum(num-1)

print(f"Your sum upto {num} is -> " + str(sum(num)))
