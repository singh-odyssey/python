# change content of file by putting comma between each letter of string 
def insert_comma():
    with open("file.txt") as f:
        lines = f.readlines()
    with open("file.txt", "w") as f:
        for line in lines:
            new_line = ",".join(line.strip())  # Insert commas
            f.write(new_line + "\n")
            print(new_line)

insert_comma()