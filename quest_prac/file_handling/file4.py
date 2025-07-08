# read last n lines of a file 
def last_lines(n):
    with open("file.txt") as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line, end='')

last_lines(5)