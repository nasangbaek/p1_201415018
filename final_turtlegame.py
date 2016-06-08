import turtle
print 'when your score is 1000, turtlrgame is turn off right?'
wn=turtle.Screen()
sangbaek1=turtle.Turtle()
sangbaek1.speed(1000)
sangbaek=turtle.Turtle()
sangbaek.shape("turtle")
sangbaek.color("Red")
sangbaek.pencolor("pink")
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
sangbaek1.write('100point')

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
score=0

def fd():
    (x,y)=sangbaek.pos()
    sangbaek.fd(50)
    global score
    if score==10:
        print 'bye'
    if(200.<x<300. and 200.<y<300.):
        print "score 100"
        score=score+1
    if(-250.<x<-150. and 0.<y<100.):
        print "score 100"
        score=score+1
    if(-200.<x<-100. and 200.<y<300.):
        print "score 100"
        score=score+1

def back():
    (x,y)=sangbaek.pos()
    sangbaek.back(50)
    global score
    if score==10:
        print 'bye'
    if(200.<x<300. and 200.<y<300.):
        print "score 100"
        score=score+1
    if(-250.<x<-150. and 0.<y<100.):
        print "score 100"
        score=score+1
    if(-200.<x<-100. and 200.<y<300.):
        print "score 100"
        score=score+1

def left():
    sangbaek.left(45)
def right():
    sangbaek.right(45)

wn.onkey(fd,"Up")
wn.onkey(back,"Down")
wn.onkey(left,"Left")
wn.onkey(right,"Right")
wn.listen()

wn.exitonclick()

