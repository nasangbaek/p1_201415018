
def drawSquareAt(size, pos):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.left(90)
        tracks.append(t1.pos())
    return tracks

drawSquareAt(100,(0,0))

def lab7():
    pos=(0,0)
    size=100
    drawSquareAt(size, pos)

def main():
    lab7()

if __name__=="__main__":
	main()