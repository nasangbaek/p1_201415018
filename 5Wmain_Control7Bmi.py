

"""
@author jsl
@since 160401
"""


def computebmi(height,weight):
    height=float(height)
    weight=float(weight)
    print height,weight
    height=height/100.0
    print height,weight
    bmi=weight/(height*height)
    print bmi
    if 18.5<bmi<25:
        print 'normal'
    elif 25.0<=bmi<30.0:
        print 'overweight'
    elif bmi<=30.0:
        print 'much overweight'
    elif bmi<18.5:
        print 'you are underweight'
    else:
        print 'error'

def lab5():
    height=174.4
    weight=63.3
    computebmi(height,weight)

def main():
    lab5()

if __name__=="__main__":
    main()