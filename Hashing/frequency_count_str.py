"""
ques -> Two lists n and m are there , find the frequency of m elements in
n list .
Constraints -> 'a'<= n[i] <='z'

"""

n = ["qweqweqwe"]
m = ["q", "a", "s"]


for i in m:
    count = n[0].count(i)
    print(f"{i} -> {count}")

# if n is a str

n = "qweqweqwe"
m = ["q", "a", "s"]


for i in m:
    count = n.count(i)
    print(f"{i} -> {count}")

# let say not using count then list will be created and hashing concept will be used or dict

hash_list = [0] * 26
for ch in n:
    ascii_val = ord(ch)
    hash_list[ascii_val - 97] += 1 # as list is only for small char , if all alphabets are there 
                                    # list will be of 127 (symbols,caps,small)
for ch in m:
    ascii_val=ord(ch)
    count=hash_list[ascii_val - 97]
    print(f"{ch}->{count}")
