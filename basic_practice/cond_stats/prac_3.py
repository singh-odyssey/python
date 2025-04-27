#write a prog to detect spam msg as the msg contain words like make money ,click here , subscribe now 

u_inp=input("Enter your msg -> ")
if ("make money" in u_inp or "subscribe" in u_inp or "click here" in u_inp):
    print("This msg may be a spam")
else:
    print("This msg is safe")
