# create a fn game and whenever game is played and high scroe is reached it updates it in hi_score.txt file 

def game():
    num = int(input("Enter any number; it will be your score -> "))
    global score
    if score == '':
        print("The file is empty. Setting the high score to your number.")
        with open("hi_score.txt", "w") as f:
            f.write(str(num))
        score = num
    else:
        score = int(score)
        if score > num:
            print("Your number is less than the high score.")
            print(f"Current High score is -> {score}")
        elif score < num:
            print("Congratulations! You have set a new high score.")
            with open("hi_score.txt", "w") as f:
                f.write(str(num))
            score = num


f=open("hi_score.txt")
score=f.read()
f.close()
game()