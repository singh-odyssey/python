# create a class programmer with attributes name, age, and language working at microsoft

class Programmer:
    def __init__(self, name, age, language, position):
        self.name=name
        self.age=age
        self.language=language
        self.position=position
    
    # def printInfo(self):
    #     print(self.name)
    #     print(self.age)
    #     print(self.language)
    #     print(self.position)


name=input("Enter the name of employee :  ")
age=int(input("Enter the age of employee :  "))
language=input("Enter the language known to  employee :  ")
pos=input("Enter the position  of employee :  ")

employee_detail = Programmer(name,age,language,pos)

with open("employee_info.txt") as file:
    old_info = file.read()
    with open("employee_info.txt", "w") as file:
        new_info = (f"{employee_detail.name}, {employee_detail.age}, {employee_detail.language}, {employee_detail.position}\n")
        file.write(old_info + new_info)

print(" ")
print(" ")

print("file updated successfully ")

with open("employee_info.txt") as file:
    info=file.read()
    print(info)
