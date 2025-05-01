# in log.html  find out if it has the word python in it

with open("log.html") as file:
    f=file.read()
    if "python" in f:
        print("word found in log file")
        position = f.find("python")
        print(f"Position of the word: {position}")
        line_number = f[:position].count('\n') + 1
        print(f"Line number of the word: {line_number}")