# fn to change cm to inches       ☆*: .｡. o(≧▽≦)o .｡.:*☆

n=int(input("Enter cm -> "))
def convert(n):
    inch = n * 0.39701 
    print(f"{n} cm = {inch} inches")

convert(n)
