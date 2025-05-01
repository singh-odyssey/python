# read file name poem and find out if it contain the word "twinkle"

f = open("poem.txt")
content = f.read()
print(content)
if "twinkle" in content:
    print("Word twinkle is found ")

f.close()