import turtle
wn=turtle.Screen()
sangbaek=turtle.Turtle()

sel=raw_input("Triangle or Square(T or S):")

size=100
if sel=='T':
    sides=3
    angle=120
elif sel=='S':
    sides=4
    angle=90
for x in range(0,sides):
 sangbaek.fd(size)
 sangbaek.right(angle)

sangbaek.speed(1)


