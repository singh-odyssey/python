# reverse list using recursion .


def reverse_list(x: list, left, right) -> list:
    if left >= right:
        return x
    x[left], x[right] = x[right], x[left]
    return  reverse_list(x, left + 1, right - 1)

x=[1,2,3,4,5]
left=0
right=len(x)-1
print(reverse_list(x,left,right))

# Time Complexity  -- O(n)
# Space Complexity -- O(n)


# reversing using while loop


while left<=right:
    x[left],x[right]=x[right],x[left]
    left+=1
    right-=1

print(x)

# Time Complexity  -- O(n)
# Space Complexity -- O(1)
