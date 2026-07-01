# finding the second largest element in array without sorting .


def sec_large(arr: list) -> int:
    largest = float("-inf")
    s_largest = float("-inf")
    for i in range(len(arr)):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i]
    return s_largest


arr = [1, 2, 4, 8, 7, 3, 10]
print(sec_large(arr))
# Time Complexity  -- O(n)
# Space Complexity -- O(1)
