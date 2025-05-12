#print 3 , 5 , 7 element from list using enumerated

l=[1,2,3,4,5,6,7]

for index, value in enumerate(l):
    if index in [2, 4, 6]:
        print(value)

