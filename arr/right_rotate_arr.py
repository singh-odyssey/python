# right rotate an array by K .


# brute force 1 (without using buildin fn)
def rr(arr: list, k: int) -> list:
    length_of_arr = len(arr)
    count = 0
    k = k % length_of_arr
    if (k % length_of_arr) == 0:
        return arr
    while count < k:
        temp = arr[length_of_arr - 1]
        for i in range(length_of_arr - 1, -1, -1):
            if i == 0:
                arr[i] = temp
            else:
                arr[i] = arr[i - 1]

        count += 1
    return  


# Time Complexity  -- O(N*k)  ~ O(N^2)   ex - k=999999 and N=1000000 -> k=N-1 ~N 
# Space Complexity -- O(1)


# brute force 2

def rr(arr: list, k: int) :
    k = k % len(arr)
    if k==len(arr):
        return
    for _ in range(k):
        e = arr.pop()
        arr.insert(0,e)


# Time Complexity  -- O(N*k)
# Space Complexity -- O(1)

# better (using slicing)
def rr(arr,k):
    n-=len(arr)
    k = k % n
    if k==len(arr):
        return
    arr[:]=arr[n-k:]+arr[:n-k]

# Time Complexity  -- O(N)
# Space Complexity -- O(1)

# optimal
def rr(arr,left,right):
    n=len(arr)
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        righ-=1
    k=3
    rr(arr,n-k,n-1) #reverse last k elements
    rr(arr,0,n-k-1) #reverse remaining elements
    rr(arr,0,n-1) #reverse whole arr

# Time Complexity  -- O(N)
# Space Complexity -- O(1)
