
x1=list()
import turtle
wn=turtle.Screen()

def drawSquareAt(size, pos):
    sangbaek=turtle.Turtle()
    sangbaek.penup()
    sangbaek.setpos(pos)
    sangbaek.pendown()
    for i in range(0,4):
        sangbaek.forward(size)
        sangbaek.left(90)
        x1.append(sangbaek.pos())
    print x1


def lab7():
    pos=(0,0)
    size=100
    drawSquareAt(size, pos)
    print x1

def main():
    lab7()

if __name__=="__main__":
	main()