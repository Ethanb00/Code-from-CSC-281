#Turtle Graphics Art Project
#By: Ethan Bennett

import turtle 
wn = turtle.Screen()
wn.bgcolor("light blue")
brooks = turtle.Turtle()
brooks.speed(0)

def house():
    brooks.color('brown')
    brooks.begin_fill()
    for i in range(4):            #builds the house exterior
        brooks.forward(100)
        brooks.left(90)
    brooks.end_fill()
        
    brooks.color('black')
    brooks.penup                  #puts brooks in a position to begin drawing roof
    brooks.left(90)
    brooks.forward(100)
    brooks.pendown()

    brooks.color('brown')
    brooks.begin_fill()
    for i in range(2):            #draws roof
        brooks.right(60)
        brooks.forward(59)
    brooks.end_fill()
    
    brooks.color('black')
    brooks.penup()                #moves brooks to the position of right window
    brooks.right(60)
    brooks.forward(25)
    brooks.right(90)
    brooks.forward(25)
    brooks.pendown()

    brooks.color('yellow')
    brooks.begin_fill()
    for i in range(4):            #draws right window
        brooks.forward(15)
        brooks.left(90)
    brooks.end_fill()

    brooks.color('black')
    brooks.penup()                #moves to location of the left window
    brooks.forward(40)
    brooks.pendown()

    brooks.color('yellow')
    brooks.begin_fill()
    for i in range(4):            #draws second window
        brooks.forward(15)
        brooks.left(90)
    brooks.end_fill()
    
    brooks.color('black')
    brooks.penup()                #moves the location of the door
    brooks.left(90)
    brooks.forward(50)
    brooks.left(90)
    brooks.forward(5)
    brooks.pendown()

    brooks.color('gray')
    brooks.begin_fill()
    for i in range(2):            #draws door
        brooks.forward(15)
        brooks.right(90)
        brooks.forward(25)
        brooks.right(90)
    brooks.end_fill()

    brooks.color('black')
    brooks.penup()                #moves to top right corner of the house
    brooks.forward(60)
    brooks.left(90)
    brooks.forward(75)
    brooks.right(45)
    brooks.pendown()

    brooks.color('brown')
    brooks.begin_fill()
    brooks.forward(23)            #extends wall out and to the right, down, and down to the left
    brooks.right(135)
    brooks.forward(100)
    brooks.right(45)
    brooks.forward(23)
    brooks.end_fill()

    brooks.penup()               #moves to the apex of the roof
    brooks.right(135)
    brooks.forward(100)
    brooks.left(60)
    brooks.forward(59)
    brooks.right(120)
    
    brooks.pendown()             #extends roof out and connects it to the wall
    brooks.color('red')
    brooks.begin_fill()
    brooks.forward(26)
    brooks.right(60)
    brooks.forward(52)
    brooks.right(100)
    brooks.forward(26)
    brooks.end_fill()
    brooks.penup()
    brooks.color('black')
    brooks.left(100)
    brooks.forward(60)

def sun():
    brooks.backward(300)         #draws the sun!
    brooks.pendown()
    brooks.color('yellow')
    brooks.begin_fill()
    brooks.circle(75)
    brooks.end_fill()

def road():
    brooks.color('black')        #draws the asphault
    brooks.penup()
    brooks.right(50)
    brooks.forward(300)
    brooks.right(100)
    brooks.forward(500)
    brooks.right(180)
    brooks.pendown()
    brooks.color('black')
    brooks.begin_fill()
    for i in range(2):
        brooks.forward(1000)
        brooks.right(90)
        brooks.forward(50)
        brooks.right(90)
    brooks.end_fill()

def lanemarker():
    brooks.penup()             #goes to location of lane markings
    brooks.right(90)
    brooks.forward(20)
    brooks.left(90)


def lanes():                     #paints lane markings
    brooks.pendown()          
    brooks.color('yellow')
    brooks.begin_fill()
    for i in range(2):
        brooks.forward(50)         
        brooks.right(90)
        brooks.forward(5)
        brooks.right(90)
    brooks.end_fill()
    brooks.penup()
    brooks.forward(100)
    brooks.pendown() 

def grass():
    brooks.color("black")  #makes some pretty grass
    brooks.penup()
    brooks.left(90)
    brooks.forward(20)
    brooks.pendown()
    brooks.color('dark green')
    brooks.begin_fill()
    for i in range(2):
        brooks.forward(79)
        brooks.left(90)
        brooks.forward(1000)
        brooks.left(90)
    brooks.end_fill()
    brooks.penup()
    brooks.forward(79)
    brooks.left(90)
    brooks.forward(345)
    brooks.right(135)
    brooks.pendown()
    brooks.begin_fill()
    brooks.forward(23)
    brooks.right(45)
    brooks.forward(330)
    brooks.right(90)
    brooks.forward(23)
    brooks.end_fill()
    brooks.penup()
    brooks.color('black')
    brooks.right(180)
    brooks.forward(23)
    brooks.left(90)
    brooks.forward(447)
    brooks.color('dark green')
    brooks.pendown()
    brooks.begin_fill()
    for i in range(2):
        brooks.forward(548)
        brooks.left(90)
        brooks.forward(23)
        brooks.left(90)
    brooks.end_fill()

def fence():                       #draws a white picket fence along the edge of the house
    brooks.penup()
    brooks.color('black')
    brooks.forward(500)
    brooks.right(90)
    brooks.color('white')
    brooks.begin_fill()
    for i in range(34):
        for i in range(2):
            brooks.forward(25)
            brooks.right(90)
            brooks.forward(5)
            brooks.right(90)
        brooks.right(90)
        brooks.forward(15)
        brooks.left(90)
    brooks.end_fill()        
    brooks.right(90)
    brooks.penup()
    brooks.forward(110)
    brooks.pendown()
    brooks.left(90)
    brooks.begin_fill()
    for i in range(22):
            for i in range(2):
                brooks.forward(25)
                brooks.right(90)
                brooks.forward(5)
                brooks.right(90)
            brooks.penup()
            brooks.right(90)
            brooks.forward(15)
            brooks.left(90)
            brooks.pendown()
    brooks.end_fill()
    brooks.penup()
    brooks.forward(12)
    brooks.left(90)
    brooks.forward(10)
    brooks.pendown()
    brooks.pensize(3)
    brooks.forward(325)
    brooks.penup()
    brooks.forward(118)
    brooks.pendown()
    brooks.forward(500)
    


#Let's Draw!!

house()
sun()
road()
lanemarker()
for i in range(10):
    lanes()
grass()
fence()

wn.exitonclick()