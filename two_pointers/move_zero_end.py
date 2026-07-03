# move zeros to end in arr .
# brute force 

def move(arr:list):
    arr2=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            arr2.append(arr[i])
    for i in range(len(arr2)):
        arr[i]=arr2[i]
    for i in range(len(arr2),len(arr)):
        arr[i]=0
    print(arr)

move([1,2,3,0,0,0,45,0])

# Time Complexity  -- O(n)
# Space Complexity -- O(n)


# optimal 
def move(arr:list):
    #edge case 1
    if len(arr)==1:
        return
    i=0 
    j=0
    while i<len(arr):
        if arr[i]==0:
            break
        i+=1
    #edge case 2
    if i==len(arr):
        return
    j=i+1
    while j<len(arr):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    print(arr)

move([0,1,2,3,0,0,0,45,0])


# Time Complexity  -- O(n)
# Space Complexity -- O(1)