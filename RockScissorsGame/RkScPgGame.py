import random
l=["rock","scissor","paper"]


while True:
    ccount=0
    ucount=0
    uc=int(input('''
    1 : start game
    2 : Exit
    '''))
    if uc==1:
        for i in range(1,6):
            uin=int(input('''
            1 : rock
            2 : scissor
            3 : paper
            '''))
            if uin==1:
                uchoice="rock"
            elif uin==2:
                uchoice="scissor"
            elif uin==3:
                uchoice="paper"
            cchoice=random.choice(l)
            if uchoice==cchoice:
                print("user choice",uchoice)
                print("computer choise",cchoice)
                print("match Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice == "rock" and cchoice == "scissor") or(uchoice == "paper" and cchoice == "rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("user choice", uchoice)
                print("computer choise", cchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("user choice", uchoice)
                print("computer choise", cchoice)
                print("computer win")
                ccount= ccount+1
        if ucount==ccount:
            print('''-------------
            Computer Score''', ccount)
            print("User Score", ucount)
            print("---Final Match Draw---")
        elif ucount>ccount:
            print('''-------------
            Computer Score''', ccount)
            print("User Score",ucount)
            print("---You Win Final Match---")
        else:
            print('''-------------
            Computer Score''', ccount)
            print("User Score", ucount)
            print("---Computer Win Final Match---")
    else:
        break
