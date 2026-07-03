# find missing number in arr acc to len 

# brute force 
def is_missing(nums):
    arr=[]
    n=len(nums)
    for i in range(n+1):
        arr.append(i)
    for i in arr:
        if i not in nums:
            return i

print(is_missing([0,1,2]))

# Time Complexity  -- O(n^2)
# Space Complexity -- O(n)

# optimise
def is_missing(nums):
    n=len(nums)

    n_sum=((n*(n+1))//2)  # sum of n natural num
    actual_sum=sum(nums)

    if n_sum==actual_sum:
        return 0
    else:
        diff =n_sum-actual_sum
    return diff

print(is_missing([3,1,2]))

# Time Complexity  -- O(n)
# Space Complexity -- O(1)