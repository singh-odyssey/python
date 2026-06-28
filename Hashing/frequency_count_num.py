"""
ques -> Two lists n and m are there , find the frequency of m elements in
n list .
Constraints -> 1<=n[i]<=10
               n can have 10^8 elements
               m can have 10^8 elements .
"""

# brute force

n = [1, 2, 3, 4, 5, 4, 3, 2, 5, 8, 10]
m = [3, 2, 1, 54, 9, 4, 7, 8]


for num in m:
    count = 0
    for i in n:
        if num == i:
            count += 1
    print(f"{num}->{count}")

# Time Complexity -- O(n*m) 10^8 * 10^8 = 10^16
# Space Complexity -- O(1)


# optimised 1
# using a hashlist approach (only valid since we know the range is from 1 to 10)

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
for i in m:
    if i < 1 or i > 10:
        print(f"{i} -> 0")
    else:
        print(f"{i}-> {hash_list[i]}")

# optimised 2
# using dict (if we are not having range and numbers can be anything )

freq_dict = {}
for i in n:
    freq_dict[i] = freq_dict.get(i, 0) + 1

for i in m:

    print(f"{i} -> {freq_dict.get(i,0)}")
