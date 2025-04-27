#create table of user input number
num=int(input("Enter number -> "))
end_point=int(input("Enter the number upto where you want the table -> "))

for i in range(1, end_point + 1):
    print(num * i)
