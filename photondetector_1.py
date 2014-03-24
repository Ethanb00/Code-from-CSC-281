#Ethan Bennett, Jamie Darken

from random import uniform
from math import pi, tan, cos, sin,radians,degrees,sqrt
import turtle


def Graphics():
    particle = turtle.Turtle()
    particle.speed(3)
    particle.penup()
    return particle

def buildContainer(wn):
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

def goTo(particle,x,y,angle):           
    particle.penup()
    particle.setpos(x,y)
    particle.pendown()
    particle.left(angle)    
    return particle
            
def makeParticle():                    #makes a particle appear in a random location
    x = uniform(0,100)
    y = uniform(0,100)
    angle = uniform(0,360)
    m = tan(radians(angle))
    b = y - (m*x)
    return (x,y),angle,m,b

def detectorTest(newM,newB):
    for i in range(11):
        if 0 <= newM*i+newB <= 10:
            return 'Hit'
        else:
            return 'Miss'
        
def checkHit(particle,detect,draw):
    if detect=='Hit':
        if draw == True:
            particle.clear()
        return True    
    x,y=particle.xcor(),particle.ycor()
    if 0<x<10 and 0<y<10:
        if draw == True:
            particle.clear()        
        return True
    if particle.distance(0,0)<=sqrt(200):
        if draw == True:
            particle.clear()
        return True    
        
def wallHit(angle,m,b,particle,detect,draw):
    detect = detectorTest(m,b)    
    if checkHit(particle,detect,draw) == True:
        return True
    y1 = m*100+b
    y2 = m*0+b 
    x1 = (100-b)/m
    x2 = (0-b)/m
    if angle >= 270:
        newData = wallHit4(x,y,x2,y1,angle,m,b,particle,draw)
    elif 180 <= angle < 270:
        newData = wallHit3(x,y,x2,y2,angle,m,b,particle,draw)
    elif 90 <= angle <= 180:
        newData = wallHit2(x,y,x1,y2,angle,m,b,particle,draw)
    elif angle < 90:
        newData = wallHit1(x,y,x1,y1,angle,m,b,particle,draw)
    prob = uniform(1,100)
    if prob >= 101:
        if draw == True:
            particle.clear()                    
        return False      
    else:
        return wallHit(newData[2],newData[3],newData[4],particle,newData[6],draw)

def wallHit1(x,y,x1,y1,angle,m,b,particle,draw):
    if y1 <= 100:
        distance = (100-x)/cos(radians(angle))
        particle.forward(abs(distance))
        particleAngle = 2*(90-angle)
        particle.left(particleAngle)
    elif y1 > 100:
        distance = (100-y)/sin(radians(angle))
        particle.forward(abs(distance))
        particleAngle = 2*angle
        particle.right(particleAngle)
    if draw == True:
        particleDraw()
    newX,newY = distance*cos(radians(angle)),distance*sin(radians(anglle))
    newM = tan(radians(particleAngle))
    newB = newY - (newM*newX)
    detect = detectorTest(newM,newB)    
    result = [newX, newY, particleAngle, newM, newB,particle,detect,draw]
    return result

def wallHit2(x,y,x1,y2,angle,m,b,particle,draw):
    if y2 <= 100:
        distance = x/cos(radians(angle))
        particle.forward(abs(distance))
        particleAngle = 2*(90-(180-angle))
        particle.right(particleAngle)
    elif y2 > 100:
        distance = (100-y)/sin(radians(angle))
        particle.forward(abs(distance)) 
        particleAngle = 2*(180-angle)
        particle.left(particleAngle)    
    angle = particle.heading()        
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)    
    result = [newX, newY, angle, newM, newB,particle,detect,draw]
    return result

def wallHit3(x,y,x2,y2,angle,m,b,particle,draw):
    if  y2 >= 0:
        distance = x/cos(radians(angle-180))
        particle.forward(distance)
        particleAngle = 90
        particle.left(particleAngle)
    elif y2 < 0:
        distance = y/sin(radians((angle-180)))
        particle.forward(abs(distance))
        particleAngle = (2*angle)
        particle.right(particleAngle)
    angle = particle.heading()    
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)  
    result = [newX, newY, angle, newM, newB,particle,detect,draw]
    return result  

def wallHit4(x,y,x2,y1,angle,m,b,particle,draw):
    if y1 >= 0:
        distance = (100-x)/cos(radians(360-angle))
        particleAngle = 2*(90-(360-angle))
        particle.right(particleAngle)
    elif y1 < 0:
        distance = y/sin(radians(360-angle))
        particle.forward(abs(distance))  
        particleAngle = (360-angle)+(.5*(180-(360-angle)))
        particle.left(particleAngle)
    angle = particle.heading()    
    newX,newY = particle.xcor(),particle.ycor()
    newM = particleSlope(angle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, angle, newM, newB,particle,detect,draw]
    return result  

def main(trials,draw):
    failure,success = 0,0
    if draw == True:
        wn = turtle.Screen()    
        buildContainer(wn)        
        particle = Graphics()
    for i in range(trials):
        (x,y),angle,m,b = makeParticle()[0],makeParticle()[1],makeParticle()[2],makeParticle()[3]
        if particle == True:
            particle = goTo(particle,x,y,angle)
        result = wallHit(angle,m,b,particle,draw)
        if result == False:
            failure += 1
        elif result == True:
            success += 1
    wn.exitonclick()
    efficiency = success / trials
    return efficiency