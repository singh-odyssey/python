# display a/b if b=0 handle it by ZeroDivisionError

a=int(input("Enter a -> "))
b=int(input("Enter b -> "))

try:
    print(a/b)
except ZeroDivisionError as e:
    print(f"Error -> {e}")