import random
userchoice=raw_input('R is Rock,P is Paper,S is Scissors:')
computerchoice=random.randint(1,3)

if userchoice=='R':
    if computerchoice==2:
        print 'lose'
    elif computerchoice==3:
        print 'win'
    else:
        print 'draw'
elif userchoice=='P':
    if computerchoice==1:
        print 'win'
    elif computerchoice==3:
        print 'lose'
    else:
        print 'draw'
elif userchoice=='S':
    if computerchoice==1:
        print 'lose'
    elif computerchoice==2:
        print 'win'
    else:
        print 'draw'
