import random

rock=1
paper=2
scissor=3
l=["rock","paper","scissor"]
def resultGame(user):
    com=random.randint(1,3)
    if user==com:
        print("Match tie")
        print("Computer:",l[com-1])
        print("User:",l[user-1])
    else:
        if user==1:
            if com==3:
                print("you win")
            else:
                print("you loss")
            print("Computer:",l[com-1])
            print("User:",l[user-1])
        if user==2:
            if com==1:
                print("you win")
            else:
                print("you loss")
            print("Computer:",l[com-1])
            print("User:",l[user-1])
        if user==3:
            if com==2:
                print("you win")
            else:
                print("you loss")
            print("Computer:",l[com-1])
            print("User:",l[user-1])
print("Enter your choice")
print("1 for Rock")
print("2 for Paper")
print("3 for Scissor")
print("4 quit")
while True:
    user=int(input("Choose your choice:"))
    if user>=4:
        break
    else:
        resultGame(user)
