#sum of n natural number 

num=int(input("Enter the number upto where u wanna sum of natural number -> "))
sum_of_numbers = 0
for i in range(1, num+1):
    sum_of_numbers += i
print(f"Your sum upto {num} natural number is -> {sum_of_numbers}")