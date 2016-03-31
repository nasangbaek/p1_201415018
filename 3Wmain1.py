
marks=raw_input("enter marks")
print marks

marks=float(marks)
print marks

computergrade(marks)

def computergrade(marks):
    if(90<=marks and marks<=100):
        grade='a'
    elif(80<=marks and marks<=90):
        grade='b'
    elif(70<=marks and marks<=80):
        grade='c'
    elif(60<=marks and marks<=70):
        grade='d'
    else:
        grade='f'
    return grade

def lab1():
    marks=raw_input("enter marks")
    marks=float(marks)
    mygrade=computergrade(marks)
    print mygrade

def main():
    lab1()