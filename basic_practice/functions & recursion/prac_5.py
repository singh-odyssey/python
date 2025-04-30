# print inverted half pyramid for n input by user

n=int(input("Enter the depth of pyramid -> ")) # ☆*: .｡. o(≧▽≦)o .｡.:*☆

def pyramid(n):
    for i in range(n, 0, -1):
        print(" * " * i)

pyramid(n)


