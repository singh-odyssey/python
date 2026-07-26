#  two sum problem


# brute force .
def twosum(nums, target):
    i = 0
    while i < len(nums) - 1:
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1
        i += 1


# Time Complexity  -- O(n^2)
# Space Complexity -- O(1)


# optimal solution --using dict
def twosum(nums: list, target: int):
    hash_map = {}
    for i in range(len(nums)):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i
    


# Time Complexity  -- O(n)
# Space Complexity -- O(n)
