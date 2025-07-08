# python prog to append text to a file and show it

def append(s):
    with open("file.txt",'a') as f:
        f.write(s)
        with open ("file.txt",'r') as f2:
            print(f2.read())


append("\nthis is append text")
