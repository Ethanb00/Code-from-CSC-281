#import turtle
#wn = turtle.Screen()
#mike = turtle.Turtle()

#def drawp(n):
#    for i in range(n):
#        mike.forward(10)
#        mike.left(360/n)

#for n in(3,4,5,6,7,8,9,10):
#    mike.penup()
#    mike.forward(20)
#    mike.pendown()
#    drawp(n)


for i in range(1,11):
    if i % 2 == 1:
        j=i*'odd '
    else:
        j = i*'even '
    print(j)