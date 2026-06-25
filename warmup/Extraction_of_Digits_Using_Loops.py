# number of digits


def count_digits(x: int) -> list:
    nums: list = []

    edge_case: int = 0
    if x == edge_case:
        return 0
    
    while x > 0:
        remainder: int = x % 10
        x = x // 10
        nums.append(remainder)
    return nums


print(count_digits(123456789))

# Time Complexity -- O(log₁₀(x))
# Space Complexity -- O(1)