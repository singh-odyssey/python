#  finding the largest element in array .

# brute force


def largest(arr: list) -> int:
    arr.sort()
    n = len(arr)
    large_num = arr[n - 1]
    return large_num

arr = [1, 2, 4, 8, 7, 3, 10]

# Time Complexity  -- O(n logn)
# Space Complexity -- O(1)


# optimal
def largest(arr: list) -> int:
    x = 0
    temp = arr[0]
    while x <= (len(arr) - 1):
        if arr[x] > temp:
            temp = arr[x]
            x += 1
        else:
            x += 1

    return temp

print(largest(arr))


# Time Complexity  -- O(n)
# Space Complexity -- O(1)



