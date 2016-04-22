import turtle
wn=turtle.Screen()
sangbaek1=turtle.Turtle()
sangbaek=turtle.Turtle()
sangbaek1.speed(100)
x=float()
y=float()

sangbaek1.penup()
sangbaek1.fd(400)
sangbaek1.left(180)
for x in range(9):
    sangbaek1.write('100')
    sangbaek1.fd(100)
sangbaek1.penup()
sangbaek1.goto(0,400)
sangbaek1.left(90)
for x in range(9):
    sangbaek1.write('100')
    sangbaek1.fd(100)
sangbaek1.goto(200,200)
sangbaek1.left(90)
sangbaek1.pendown()
sangbaek1.write('100point')
for x in range(4):
    sangbaek1.fd(100)
    sangbaek1.left(90)
sangbaek1.penup()
sangbaek1.goto(-200,200)
sangbaek1.pendown()
sangbaek1.setheading(0)
sangbaek1.write('150point')
for x in range(3):
    sangbaek1.fd(100)
    sangbaek1.left(120)
sangbaek1.penup()
sangbaek1.goto(-200,0)
sangbaek1.pendown()
sangbaek1.write('100point')
sangbaek1.circle(50)
sangbaek1.penup()
(x,y)=sangbaek.pos()

def fd():
    x=float()
    y=float()
    (x,y)=sangbaek.pos()
    sangbaek.fd(50)
    if(200.<x<300. and 200.<y<300.):
        print "your score is 100"
    if(-250.<x<-150. and 0.<y<100.):
        print "your score is 100"

def back():
    sangbaek.back(50)
def left():
    sangbaek.left(45)
def right():
    sangbaek.right(90)


wn.onkey(fd,"Up")
wn.onkey(back,"Down")
wn.onkey(left,"Left")
wn.onkey(right,"Right")
wn.listen()

wn.exitonclick()

