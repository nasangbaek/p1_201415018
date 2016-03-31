import turtle
wn=turtle.Screen()
sangbaek=turtle.Turtle()

sides=10
size=10
bigger=10
angle=90

def makeSwirlSquare(size,bigger,sides,angle):
    for i in range(0,sides):
        if (i%2):
            size=size+bigger
            sangbaek.fd(size)
            sangbaek.right(angle)

makeSwirlSquare(10,10,50,90)

wn.exitonclick()