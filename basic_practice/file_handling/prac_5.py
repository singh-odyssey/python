#replace words from file by comparing it from a list

bad_words=["bura","abuse","bad"]

with open("replace2.txt") as f:
    oldF=f.read()
    for i in bad_words:
        if i in oldF:
            oldF = oldF.replace(i, "#####")
    newF = oldF
    with open("replace2.txt", "w") as f:
        f.write(newF)
        print(newF)
        