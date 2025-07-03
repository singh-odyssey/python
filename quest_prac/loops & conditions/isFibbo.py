# is the entered number in the fibbonachi sequence or not
def isFibbo(num):
    n1, n2 = 0, 1
    if num == n1 or num == n2:
        return True
    while n2 < num:
        nth = n1 + n2
        n1, n2 = n2, nth
        if num == nth:
            return True
    return False
# Test the function
if __name__ == "__main__":
    number = int(input("Enter a number to check if it is in the Fibonacci sequence: "))
    if isFibbo(number):
        print(f"{number} is in the Fibonacci sequence.")
    else:
        print(f"{number} is not in the Fibonacci sequence.")