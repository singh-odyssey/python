# merge two sorted arr with non repeating elements from both arr .


def merge_arr(nums1,nums2):
    res=[]   
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j] :
            if len(res)==0 or nums1[i]!=res[-1]:
                res.append(nums1[i])
            i+=1
        else:
             if len(res)==0 or nums2[j]!=res[-1]:
                res.append(nums2[j])
             j+=1

    while i <len(nums1):
         if len(res)==0 or nums1[i]!=res[-1]:
                res.append(nums1[i])
         i+=1
    while j <len(nums2):
         if len(res)==0 or nums2[j]!=res[-1]:
                res.append(nums2[j])
         j+=1

    print(res)
arr1=[1,2,3,3,3]
arr2=[4,5,6]

merge_arr(arr1,arr2)

# Time Complexity  -- O(n+m)
# Space Complexity -- O(n+m)
