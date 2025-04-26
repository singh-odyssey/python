#take marks of a student as a user input and show them in sorted order

marks=[]

m1=int(input("Enter your marks -> ")) # note if here we don't type cast it in int then sorting will be done according to string
marks.append(m1)                      # which is asci values
m2=int(input("Enter your marks -> "))
marks.append(m2)
m3=int(input("Enter your marks -> "))
marks.append(m3)
m4=int(input("Enter your marks -> "))
marks.append(m4)

marks.sort()
print(marks)
