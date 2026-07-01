# remove duplicates from sorted array , 
# return unique elements .

# brute force

def remove(arr: list) -> int:
    n=len(arr)
    freq_map={}
    for i in range (n):
        freq_map[arr[i]]=0
    k=0
    for i in freq_map:
        arr[k]=i 
        k+=1
    return k

arr=[]
print(remove(arr))

# Time Complexity  -- O(2n) ~ O(n)
# Space Complexity -- O(n)

# optimal 

def remove(arr:list)->int:
    n=len(arr)
    i=0
    j=i+1
    while j<n:
        if n==1:    #edge case
            return n   
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        j+=1
    return i+1

arr=[]
print(remove(arr))


# Time Complexity  -- O(n) 
# Space Complexity -- O(1)