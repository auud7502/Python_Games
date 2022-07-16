import random
u=0 #user points
c=0 #computer points
r=0 #present round
round = ""
while len(str(round)) == 0:
    round = input("Give the number of rounds to be played :")
rounds =int(round)
options = ['rock','paper','scissor']
if rounds>0:
    for r in range(0,rounds,1):
        userchoice = input("What is your choice? :")
        if userchoice in options:
            compchoice = random.choice(options)
            print("Computer choice is :"+compchoice)
            if userchoice.lower() == "rock":
                if compchoice == "rock":
                    print("Nobody gets a point!")
                elif compchoice == "paper":
                    print("Your opponent gets a point!")
                    c += 1
                elif compchoice == "scissor":
                    print("You get a point!")
                    u += 1
            elif userchoice.lower() == "paper":
                if compchoice == "rock":
                    print("You get a point!")
                    u += 1
                elif compchoice == "paper":
                    print("Nobody gets a point!")
                elif compchoice == "scissor":
                    print("Your opponent gets a point!")
                    c += 1
            elif userchoice.lower() == "scissor":
                if compchoice == "rock":
                    print("Your opponent gets a point!")
                    c += 1
                elif compchoice == "paper":
                    print("You get a point!")
                    u += 1
                elif compchoice == "scissor":
                    print("Nobody gets a point!")

        else:
            print("You have chosen an invalid choice")
            rounds+=1
        print()
    print()
    print("Your score           :" + str(u))
    print("Yor opponent's score :" + str(c))
    print()
    if u > c:
        print("congratulations! You Win!")
    elif c > u:
        print("You have Lost! Better luck next time!")
    else:
        print("It is a tie!")
else:
    print("Invalid number of rounds")



