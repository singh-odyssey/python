# Print hollow rectangle

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(1, rows + 1):
    if i == 1 or i == rows:  # First and last rows
        print("* " * cols)
    else:  # Middle rows
        print("* " + "  " * (cols-2) + "*")
