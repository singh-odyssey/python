# print prime number in range 

checking_limit = int(input("Enter the term upto where you wanna check prime number -> "))
print("All prime numbers for the given range are:", end=" ")

for i in range(2, checking_limit + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) +1 ): # stoping range is sqrt i**0.5 is sqrt 
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
print()

# another logic for j loop 

# for j in range(2, i):
#     if i % j == 0:
#         is_prime = False
#         break