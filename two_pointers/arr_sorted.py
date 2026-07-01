# check if arr is sorted or not .


def is_sort(arr: list) -> bool:
    for i in range(len(arr)):
        if i < len(arr) - 1 and arr[i] > arr[i + 1]:
            return False
    return True


arr = [1, 2, 3, 7,5]
print(is_sort(arr))

# Time Complexity  -- O(n)
# Space Complexity -- O(1)
