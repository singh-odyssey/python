# python prog to read line by line and store it in a list

def line_by_line():
    with open("file.txt") as f:
        l=[]
        line=f.readline()
        while line:
            l.append(line.strip())
            line=f.readline()
    print(l)

line_by_line()