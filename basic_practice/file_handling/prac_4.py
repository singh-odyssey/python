#replace a particular word in file and update that file with the new content

with open("replace.txt") as f:
    oldF=f.read()
    if "hi" in oldF:
        newF=oldF.replace("hi","hola")
        with open("replace.txt","w") as f:
            f.write(newF)
            print(newF)