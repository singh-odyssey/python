# read finite number of lines from a file

def finit_lines(n):
    with open("file.txt",'r') as f:
        for i in range(n):
            print(f.readline())

finit_lines(5)