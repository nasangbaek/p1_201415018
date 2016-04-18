

def drawSquareAt(size, pos):
    global x1
    global sangbaek
    x1=list()
    import turtle
    wn=turtle.Screen()
    sangbaek=turtle.Turtle()
    sangbaek.penup()
    sangbaek.setpos(pos)
    sangbaek.pendown()
    for i in range(0,4):
        sangbaek.forward(size)
        sangbaek.left(90)
        x1.append(sangbaek.pos())
    print x1

drawSquareAt(100,(0,0))


def drawSquareAtinList():
    sangbaek.home()
    sangbaek.clear()
    for j in x1:
        sangbaek.goto(j)


def lab7():
    import turtle
    wn=turtle.Screen()
    sangbaek=turtle.Turtle()
    pos=(0,0)
    size=100
    drawSquareAt(size, pos)
    drawSquareAtinList()

def main():
    lab7()

if __name__=="__main__":
	main()