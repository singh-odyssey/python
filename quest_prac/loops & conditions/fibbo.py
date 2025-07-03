# creating  fibbonachi sequence
num=int(input("Enter numbers of terms of fibo sequence "))
n1=0
n2=1
count=2 # initializing from 2 as 2 values of seq is defined already

print("your fibbo sequence is " ,n1,n2, end=" ")

while count<=num:
    nth=n1+n2 # nth is a new term here
    print(nth,end=" ")
    n1,n2=n2,nth # updating values of n1 and n2 with each loop
    count+=1;

print()