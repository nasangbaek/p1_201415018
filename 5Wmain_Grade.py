marks=raw_input("enter mark:")

marks=float(marks)


def ComputerGrade(marks):
    if(90<=marks and marks<=100):
        print "Grade is A"
    elif(80<=marks and marks<=90):
        print "Grade is B"
    elif(70<=marks and marks<=80):
        print "Grade is C"
    elif(60<=marks and marks<=70):
        print "Grade is D"
    else:
        print "Grade is F"

ComputerGrade(marks)