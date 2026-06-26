#  finding all factors of a num .

# Better Solution
def factors(x: int) -> list:
    result: list = []
    # edge_case
    if x <= 0:
        return "invalid input"
    for i in range(1,(x//2)+1):
        if x % i == 0:
            result.append(i)
    result.append(x)        
    return result

print(factors(20))
print(factors(25))

# Time Complexity   --- O(n)
# Space Complexity  --- O(k) where k is total number of factors


# AI suggested 
# optimal Solution
import math

def factors(x: int) -> list:
    if x <= 0:
        return "invalid input"
        
    result = []
    # Loop from 1 to the square root of x
    for i in range(1, int(math.isqrt(x)) + 1):
        if x % i == 0:
            result.append(i)
            # Avoid adding the square root twice (e.g., 6 * 6 for 36)
            if i != x // i:
                result.append(x // i)
    
    return result

# Time Complexity   --- O(sqrt(n)) if sorting is done using sort function then --- O(sqrt(n)) + O(nlogn)
# Space Complexity  --- O(k) where k is total number of factors
