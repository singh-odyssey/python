#  return max consecutive ones from an array .

def max_ones(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


# Test cases
print(max_ones([1]))  # Output: 1
print(max_ones([0, 1]))  # Output: 1
print(max_ones([1, 1, 0, 1, 1, 1]))  # Output: 3

# Time Complexity  -- O(n) (one single pass)
# Space Complexity -- O(1) (only storing two integer counters)
