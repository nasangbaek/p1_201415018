

def sumOfMultiplesOf3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if i%3==0 or i%5==0:
            sum=sum+i
    print sum
    return sum



def leapyear():
    year=raw_input("input year example 1994:")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year"
    else:
        print "normal year"


def upanddown():
    import random
    sel1=random.choice(range(50))
    choicenumber=0
    sel2=-1

    while sel1!=sel2:
        sel2=raw_input('input your choice(1~50):')
        sel2=int(sel2)
        if sel1<sel2:
            print 'down'
        elif sel1>sel2:
            print 'up'
        choicenumber=choicenumber+1
    print (choicenumber, 'times example 1times,2times,3times, right?')


def lab6():
    sumOfMultiplesOf3_5(1,1000)
    leapyear()
    upanddown()

def main():
	lab6()

if __name__=="__main__":
	main()
