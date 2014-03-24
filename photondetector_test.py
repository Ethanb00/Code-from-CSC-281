#Ethan Bennett, Jamie Darken

from random import uniform
from math import pi, tan, cos, sin,radians,degrees,sqrt
import turtle


def Graphics():
    particle = turtle.Turtle()
    particle.speed(3)
    particle.penup()
    return particle

def buildContainer(wn):            #builds the box and detector
    builder = turtle.Turtle()
    builder.speed(0)
    builder.penup()
    builder.setpos(0,0)
    builder.pendown()
    for i in range(4):
        builder.forward(100)
        builder.left(90)
    for i in range(4):
        builder.forward(10)
        builder.left(90)
    builder.ht()

def goTo(particle,x,y,angle):              #particle goes to the position where it appears
    particle.penup()
    particle.setpos(x,y)
    particle.pendown()
    particle.left(angle)    
    return particle
            
def makeParticle():                    #makes a particle appear in a random location
    x = uniform(0,100)
    y = uniform(0,100)
    return (x,y)

def particleDirection():               #determines the direction of the particle
    return uniform(0,360)

def particleSlope(angle):              #determines the slope of the path the particle takes
    return tan(radians(angle))
     
def particleIntercept(m,x,y):          #determines the y-intercept of the path of the particle 
    return y - (m*x)

def detectorTest(newM,newB):
    for i in range(11):
        if 0 <= newM*i+newB <= 10:
            return 'Hit'
        else:
            return 'Miss'
        
def wallHit(angle,m,b,particle,detect='Miss'):  #determines which wall the particle hits and where
    if detect=='Hit':
        particle.clear()
        return True    
    x,y=particle.xcor(),particle.ycor()
    if 0<x<10 and 0<y<10:
        particle.clear()        
        return True
    if particle.distance(0,0)<=sqrt(200):
        particle.clear()
        return True
    y1 = m*100+b #when x=100
    y2 = m*0+b #when x=0
    x1 = (100-b)/m #when y=100
    x2 = (0-b)/m #when y=0
    if angle >= 270:
        newData = wallHit4(x,y,x2,y1,angle,m,b,particle)
    elif 180 <= angle < 270:
        newData = wallHit3(x,y,x2,y2,angle,m,b,particle)
    elif 90 <= angle <= 180:
        newData = wallHit2(x,y,x1,y2,angle,m,b,particle)
    elif angle < 90:
        newData = wallHit1(x,y,x1,y1,angle,m,b,particle)
    prob = uniform(1,100)
    if prob >= 101: #this accounts for walls that absorb 5% of the time
        particle.clear()                    
        return False      
    else:
        return wallHit(newData[2],newData[3],newData[4],particle,newData[6])

def wallHit1(x,y,x1,y1,angle,m,b,particle):
    if y1 <= 100:
        particle.goto(100,y1)
        particleAngle = 2*(90-angle)
        particle.left(particleAngle)
    if y1 > 100:
        distance = (100-y)/sin(radians(angle))
        particle.forward(abs(distance))
        particleAngle = 2*angle
        particle.right(particleAngle)
    angle = particle.heading()    
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect='Miss'
    result = [newX, newY, angle, newM, newB,particle,detect]
    return result

def wallHit2(x,y,x1,y2,angle,m,b,particle):
    if y2 <= 100:
        particle.goto(0,y2)
        particleAngle = 2*(90-(180-angle))
        particle.right(particleAngle)
    if y2 > 100:
        distance = (100-y)/sin(radians(angle))
        particle.forward(abs(distance)) 
        particleAngle = 2*(180-angle)
        particle.left(particleAngle)    
    angle = particle.heading()        
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, angle, newM, newB,particle,detect]
    return result

def wallHit3(x,y,x2,y2,angle,m,b,particle):
    if  y2 >= 0:
        particle.goto(0,y2)
        particleAngle = 2*(90-(angle-180))
        particle.left(particleAngle)
    if y2 < 0:
        distance = y/sin(radians(angle-180))
        particle.forward(abs(distance))
        particleAngle = 2*(angle-180)
        particle.right(particleAngle)
    angle = particle.heading()    
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, angle, newM, newB,particle,detect]
    return result  

def wallHit4(x,y,x2,y1,angle,m,b,particle):
    if y1 >= 0:
        particle.goto(100,y1)
        particleAngle = 2*(90-(360-angle))
        particle.right(particleAngle)
    if y1 < 0:
        distance = y/sin(radians(360-angle))
        particle.forward(abs(distance))  
        particleAngle = 2*(360-angle)
        particle.left(particleAngle)
    angle = particle.heading()    
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, angle, newM, newB,particle,detect]
    return result  

def main(trials):
    failure = 0
    success = 0
    wn = turtle.Screen()    
    buildContainer(wn)
    particle = Graphics()
    for i in range(trials):
        x,y = makeParticle()
        angle = particleDirection()
        m = particleSlope(angle)  
        b = particleIntercept(m,x,y)        
        particle = goTo(particle,x,y,angle)
        result = wallHit(angle,m,b,particle)
        if result == False:
            failure += 1
        if result == True:
            success += 1
    wn.exitonclick()
    efficiency = success / trials
    return efficiency