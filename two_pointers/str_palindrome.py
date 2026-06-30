# checking if str is palindrome using recursion .


def is_palindrome(x: str, left, right) -> bool:
    if left >= right:
        return True

    if x[left] != x[right]:
        return False
    return is_palindrome(x, left + 1, right - 1)


x = "qwqwqwqw"
left = 0
right = len(x)-1
print(is_palindrome(x, left, right))

# Time Complexity  -- O(n/2) -> O(n)
# Space Complexity -- O(n)
