#print table in reverse order 

num=int(input("Enter your number -> "))
upto=int(input("Enter upto where -> "))

for i in range(upto, 0, -1):
    print(num * i)