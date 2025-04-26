#creating empty dic... and updating its key value based on user input
dic ={}

key=input("enter the key -> ")
value =input("enter the value -> ")

key2=input("enter the key -> ")
value2 =input("enter the value -> ")

dic.setdefault(key,value)
dic.setdefault(key2,value2)
print(dic)