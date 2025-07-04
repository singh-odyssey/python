
my_list = [0, 1, 2, 3, 4 ,5]
length = len(my_list)

# Function to get a list from the last item to the second item in reverse order
def get_last_to_second(lst):
        result=lst[length:0:-1]
        print (result)

# a list that start from third item to second last item
def third_to_secondLast(lst):
    result=lst[2:length-1]
    print (result)

# fn to print only even position element 
def even_pos(lst):
    result=lst[::2]
    print (result)

def middle_of_list(lst):
    result=lst[length//2::1]
    print (result)

get_last_to_second(my_list)
third_to_secondLast(my_list)
even_pos(my_list)
middle_of_list(my_list)