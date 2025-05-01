# create table from 2 to 20 and place that table in a file 

def createTable(i):
    n = 1
    l = []
    while n <= 10:
        l.append(f"{i} x {n} = {i * n}")
        n += 1
    return l

for i in range(2, 21):
    table = createTable(i)
    with open("tables.txt", "a") as file:  
        file.write(f"Table of {i}:\n")
        file.write("\n".join(table) + "\n\n")

