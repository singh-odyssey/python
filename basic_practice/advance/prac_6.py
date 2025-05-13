# write a prog to filter out numbers from a list which are divisible by 5

l = [12, 2, 3, 4, 5, 6, 55, 10, 100]

def div(x):
    return x % 5 == 0

nums = filter(div, l)
print(list(nums))