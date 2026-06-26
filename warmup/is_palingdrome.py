#  finding if a number is  Palindrome


def is_palindrome(x: int) -> bool:
    num: int = x
    # edge case
    if num == 0:
        return True
    reverse_num: int = 0
    while num > 0:
        last_digit: int = num % 10
        num = num // 10
        reverse_num = reverse_num * 10 + last_digit
    if x == reverse_num:
        return True
    else:
        return False


print(is_palindrome(151))

# Time Complexity   --- O(log₁₀(x))
# Space Complexity  --- O(1)


# AI suggested code 
def is_palindrome(x: int) -> bool:
    if x < 0:  # Small optimization: negative numbers are never palindromes
        return False

    num: int = x
    reverse_num: int = 0
    while num > 0:
        last_digit: int = num % 10
        num = num // 10
        reverse_num = reverse_num * 10 + last_digit

    return x == reverse_num

# Time Complexity   --- O(log₁₀(x))
# Space Complexity  --- O(1)