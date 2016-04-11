
def sumlist(alist):
    x1=list()
    for i in range(0,alist):
        if i%4==0 and i%5!=0:
            x1.append(i)
    sum=0
    print x1
    for x in range(0,len(x1)):
        sum=sum+x1[x]
    print sum

def lab6():
    alist=1000
    print 'alist=1000, sumlist(alist)'
    sumlist(alist)

def main():
	lab6()

if __name__=="__main__":
	main()