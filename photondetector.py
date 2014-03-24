#Ethan Bennett, Jamie Darken

from random import uniform
from math import pi, tan, cos, sin,radians,degrees,sqrt
import turtle


def Graphics():
    particle = turtle.Turtle()
    particle.speed(0)
    particle.penup()
    return particle

def buildContainer(wn):            #builds the box and detector
    builder = turtle.Turtle()
    builder.speed(0)
    builder.penup()
    builder.setpos(0,0)
    builder.pendown()
    for i in range(4): builder.forward(100),builder.left(90)
    for i in range(4): builder.forward(10),builder.left(90)
    builder.ht()

def goTo(particle,x,y,angle):#particle goes to the position where it appears
    particle.penup()
    particle.setheading(0)
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
    """
    Returns True or False depending on if the particle's path passes through the detector
    >>> detectorTest(1,1)
    'Hit'
    >>> detectorTest(100,100)
    'Miss'
    """
    for i in range(11):
        if 0 <= newM*i+newB <= 10:
            return 'Hit'
        else:
            return 'Miss'
        
def wallHit(x,y,angle,m,b,particle,Drawing,detect):  #determines which wall the particle hits and where
    if detect=='Hit':
        if Drawing == True: particle.clear()
        return True    
    y1 = m*100+b #when x=100
    y2 = m*0+b #when x=0
    x1 = (100-b)/m #when y=100
    x2 = (0-b)/m #when y=0
    if angle >= 270:
        newData = wallHit4(x,y,x2,y1,angle,m,b,particle,Drawing)
    elif 180 <= angle < 270:
        newData = wallHit3(x,y,x2,y2,angle,m,b,particle,Drawing)
    elif 90 <= angle <= 180:
        newData = wallHit2(x,y,x1,y2,angle,m,b,particle,Drawing)
    elif angle < 90:
        newData = wallHit1(x,y,x1,y1,angle,m,b,particle,Drawing)
    while newData[2] > 360: newData[2] -= 360
    prob = uniform(1,100)
    if prob >= 96: #this accounts for walls that absorb 5% of the time
        if Drawing == True: particle.clear()                    
        return False      
    else:
        return wallHit(newData[0],newData[1],newData[2],newData[3],newData[4],particle,Drawing,newData[7])

def wallHit1(x,y,x1,y1,angle,m,b,particle,Drawing):
    if y1 <= 100:
        particleAngle = 180-2*angle
        distance = (100-x)/cos(radians(angle))
        slopeAngle = 180-angle
    if y1 > 100:
        particleAngle = 360 - 2*angle
        distance = (100-y)/sin(radians(angle))
        slopeAngle = 360-angle
    if Drawing == True: particle = wallHit1Graphics(y1,distance,particleAngle,particle)
    newX,newY = x+distance*cos(radians(angle)),y+distance*sin(radians(angle))     
    newM = particleSlope(slopeAngle)
    newB = particleIntercept(newM, newX, newY)
    detect='Miss'
    result = [newX, newY, slopeAngle, newM, newB,particle,Drawing,detect]
    return result

def wallHit1Graphics(y1,distance,particleAngle,particle):
    particle.forward(abs(distance))    
    if y1 <= 100:
        particle.left(particleAngle)
    if y1 > 100:
        particle.left(particleAngle)
    return particle

def wallHit2(x,y,x1,y2,angle,m,b,particle,Drawing):
    if y2 <= 100:
        distance = x/cos(radians(180-angle))
        particleAngle = 2*(90-(180-angle))
        slopeAngle = 180-angle
    if y2 > 100:
        distance = (100-y)/sin(radians(180-angle))
        particleAngle = 2*(180-angle)
        slopeAngle = 360-angle
    if Drawing == True: particle = wallHit2Graphics(y2,distance,particleAngle,particle)
    newX,newY = x-distance*cos(radians(180-angle)),y+distance*sin(radians(180-angle))  
    newM = particleSlope(slopeAngle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, slopeAngle, newM, newB,particle,Drawing,detect]
    return result

def wallHit2Graphics(y2,distance,particleAngle,particle):
    particle.forward(abs(distance))     
    if y2 <= 100:
        particle.right(particleAngle)
    if y2 > 100:
        particle.left(particleAngle)
    return particle

def wallHit3(x,y,x2,y2,angle,m,b,particle,Drawing):
    if  y2 >= 0:
        distance = x/sin(radians(270-angle))
        particleAngle = 2*(90-(angle-180))
        slopeAngle = 540-angle
    if y2 < 0:
        distance = y/cos(radians(270-angle))
        particleAngle = 2*(angle-180)
        slopeAngle = 360-angle
    if Drawing == True: particle = wallHit3Graphics(y2,distance,particleAngle,particle)
    newX,newY = x-distance*sin(radians(270-angle)),y-distance*cos(radians(270-angle))     
    newM = particleSlope(slopeAngle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, slopeAngle, newM, newB,particle,Drawing,detect]
    return result  

def wallHit3Graphics(y2,distance,particleAngle,particle):
    particle.forward(abs(distance))    
    if  y2 >= 0:
        particle.left(particleAngle)
    if y2 < 0:
        particle.right(particleAngle)
    return particle

def wallHit4(x,y,x2,y1,angle,m,b,particle,Drawing):
    if y1 >= 0:
        distance = (100-x)/sin(radians(angle-270))
        particleAngle = 2*(90-(360-angle))
        slopeAngle = 540-angle
    if y1 < 0:
        distance = y/cos(radians(angle-270))
        particleAngle = 2*(360-angle)
        slopeAngle = 360-angle
    if Drawing == True: particle = wallHit4Graphics(y1,distance,particleAngle,particle)        
    newX,newY = x+distance*sin(radians(angle-270)),y-distance*cos(radians(angle-270))       
    newM = particleSlope(slopeAngle)
    newB = particleIntercept(newM, newX, newY)
    detect = detectorTest(newM,newB)
    result = [newX, newY, slopeAngle, newM, newB,particle,Drawing,detect]
    return result

def wallHit4Graphics(y1,distance,particleAngle,particle):
    particle.forward(abs(distance))  
    if y1 >= 0:
        particle.right(particleAngle)
    if y1 < 0:
        particle.left(particleAngle)  
    return particle

def experiment(trials,Drawing=True): 
    failure = 0
    success = 0
    detect = ''
    if Drawing == True: 
        wn = turtle.Screen()
        buildContainer(wn)
        particle = Graphics()
    else: particle = None
    for i in range(trials):
        (x,y),angle = makeParticle(),particleDirection()
        m = particleSlope(angle)  
        b = particleIntercept(m,x,y)        
        if Drawing == True: particle = goTo(particle,x,y,angle)
        result = wallHit(x,y,angle,m,b,particle,Drawing,detect)
        if result == False:
            failure += 1
        if result == True:
            success += 1
    if Drawing == True: wn.exitonclick()
    efficiency = success / trials
    return efficiency

if __name__=='__main__':
    import doctest
    print('Testing...')
    doctest.testmod()
    print('Testing over.')