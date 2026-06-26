# finding if a number is armstrong .


def is_armstrong(x: int) -> bool:
    num1, num2 = x, x
    count = 0
    # edge_case
    if x < 0:
        return False

    while num1 > 0:
        num1 = num1 // 10
        count += 1
    total = 0
    while num2 > 0:
        last_digit = num2 % 10
        total = total + (last_digit**count)
        num2 = num2 // 10
    return total == x


print(is_armstrong(153))

# Time Complexity   --- O(log₁₀(x))
# Space Complexity  --- O(1)


# AI suggested


def is_armstrong(x: int) -> bool:
    if x < 0:
        return False

    # Get number of digits using string conversion
    count = len(str(x))

    num = x
    total = 0
    while num > 0:
        last_digit = num % 10
        total += last_digit**count
        num = num // 10

    return total == x
