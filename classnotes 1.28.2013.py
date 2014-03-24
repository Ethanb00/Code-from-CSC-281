import turtle 
wn = turtle.Screen()
wn.bgcolor("white")
sofie = turtle.Turtle() 

for i in range(6):
    sofie.forward(150)
    sofie.left(60)

wn.exitonclick()




#parentheses indicate a function or METHOD (Turtle is a method of turtle), blob.otherblob, blob is an oject,otherblob is an attribute of the object, blob.yetanotherblob(), yetanotherblob is a method of the object blob

#for i  in range(4):  #1,10 are peramiters of the function range
    #print('i =',i)
    #print('i^2 =',i*i)

#number = 0
#for month in ['January','February','March','April']:
#    number = number + 1
#    print('Month', number, 'of the year is', month)

#month = ['January','February','March','April']
#for number in range(len(month)):
#    print('Month', number+1, ' of the year is', month[number])

