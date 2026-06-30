# finding fibonacci number of particular loc using recursion .


def fibo(x , y, num ,count) -> int:
    if count == num:
        return x
    return fibo(y, x + y, num, count + 1)

print(fibo(0,1,10,0))

# Time complexity: O(n)
# Space complexity: O(n)

# AI generated .
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 10
print(f"fibonacci({n}) is {fibonacci(n)}")   

# Time complexity: O(2^n)
# Space complexity: O(n)