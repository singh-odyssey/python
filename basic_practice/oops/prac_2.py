import math

# create a class calculator capable of finding sqrt , square, cube 

def sqrt(n):
    return math.sqrt(n)
    
def cube(n):
    return (n*n*n)
    

def square(n):
    return (n*n)

class Calculator:
    def __init__(self,num):
        self.num=num
        self.sqrt_res=sqrt(self.num)        
        self.c_res=cube(self.num)        
        self.sq_res=square(self.num)        
        
    def print_res(self):
        print(f"square root of number : {self.sqrt_res} ")
        print(f"cube of number : {self.c_res} ")
        print(f"square of number : {self.sq_res} ")


num=int(input("Enter the number : "))
calc = Calculator(num)
calc.print_res()