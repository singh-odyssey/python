# write a prog to find if a student is pass or fail if total 40 % is required and 33 % is requried in each subject .
# Assume marks of 3 subject user input

marks1=int(input("Enter number of subject 1 -> "))
marks2=int(input("Enter number of subject 2 -> "))
marks3=int(input("Enter number of subject 3 -> "))

total=((marks1+marks2+marks3)/300)*100
sub1=(marks1/100 )*100
sub2=(marks2/100 )*100
sub3=(marks3/100 )*100

if(total>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print(f"Student is passed percentage -> {total}")
else:
    print("Student is not passed ")