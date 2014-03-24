#Ethan Bennett, Jamie Darken

from random import uniform
from math import pi, tan, cos, sin
import turtle

detectorCorner1 = (0,10)
detectorCorner2 = (10,0)

def Graphics():
    particle = turtle.Turtle()
    particle.speed(3)
    particle.penup()
    return particle

def buildContainer(wn,detectorCorner1):            #builds the box and detector
    builder = turtle.Turtle()
    builder.speed(0)
    builder.penup()
    builder.setpos(0,0)
    builder.pendown()
    for i in range(4):
        builder.forward(100)
        builder.left(90)
    for i in range(4):
        builder.forward(detectorCorner1[1])
        builder.left(90)
    builder.ht()

def goTo(particle,x,y,angle):              #particle goes to the position where it appears
    particle.goto(x,y)
    particle.pendown()
    particle.radians()    
    particle.left(angle)    
    return particle
            
def makeParticle():                    #makes a particle appear in a random location
    x = uniform(0,100)
    y = uniform(0,100)
    return (x,y)

def particleDirection():               #determines the direction of the particle
    return uniform(0,2*pi)

def particleSlope(angle):              #determines the slope of the path the particle takes
    return tan(angle)
     
def particleIntercept(m,x,y):          #determines the y-intercept of the path of the particle 
    return y - (m*x)

def detectorHit(m,b,detectorCorner1):                  #determines if the particle hits the detector
    for x in range(detectorCorner1[0],detectorCorner1[1]+1):
        y= m*x+b
        if y <= detectorCorner1[1]:
            return True
    return False

def wallHit(x,y,angle,m,b,particle):                #determines which wall the particle hits and where
    if detectorHit(m,b,detectorCorner1) == False:
        y1 = m*100+b #when x=100
        y2 = m*0+b #when x=0
        x1 = (100-b)/m #when y=100
        x2 = (0-b)/m #when y=0
        if angle >= (3*pi)/2:
            newData = wallHit4(x,y,x2,y1,angle,m,b,particle)
        if pi <= angle < (3*pi)/2:
            newData = wallHit3(x,y,x2,y2,angle,m,b,particle)
        if pi/2 <= angle <= pi:
            newData = wallHit2(x,y,x1,y2,angle,particle,m,b)
        if angle < pi/2:
            newData = wallHit1(x,y,x1,y1,angle,particle,m,b)
        prob = uniform(1,100)
        if prob >= 96: #this accounts for walls that absorb 5% of the time
            return False
        else:
            return wallHit(newData[0], newData[1], newData[2], newData[3], newData[4],particle)
    else:
        return True
    
    
def wallHit1(x,y,x1,y1,angle,particle,m,b):
    #angle<pi/2, look at x1 and y1
    if x-x1 < y-y1:
        #it hits y=100, new starting point is (x1,100)
        newX, newY = x1, 100
        newAngle = pi - angle               
    else:
        #it hits x=100, new starting point is (100,y1)
        newX, newY = 100, y1
    wallHit1Graphics(m,b,angle,x,y,particle)
    newAngle = pi - angle
    newM = particleSlope(newAngle)
    newB = particleIntercept(newM, newX, newY)
    result = [newX, newY, newAngle, newM, newB]
    particle.left(newAngle)        
    return result

def wallHit1Graphics(m,b,angle,x,y,particle):
    y_new = (m*100)+b
    if y_new > 100:
        h = (100-y)/sin(angle)
        particle.forward(abs(h))
    else:
        h = (100-x)/cos(angle)
        particle.forward(abs(h))
    return particle

def wallHit2(x,y,x1,y2,angle,particle,m,b):
    # angle is between pi and pi/2, look at x1 and y2
    if x-x1 < y-y2:
        #it hits y=100, new starting point is (x1,100)
        newX, newY = x1, 100
    else:
        #it hits the y axis, new starting point is (0,y2)
        newX, newY = 0, y2
    wallHit2Graphics(m,b,angle,x,y,particle)
    newAngle = pi - angle
    newM = -particleSlope(newAngle)
    newB = particleIntercept(newM, newX, newY)
    result = [newX, newY, newAngle, newM, newB]
    particle.left(newAngle)        
    return result

def wallHit2Graphics(m,b,angle,x,y,particle):
    y_new = m*0+b
    if y_new > 100:
        h = (100-y)/sin(angle)
        particle.forward(abs(h))
    else:
        h = x/cos(angle)
        particle.forward(abs(h))
    return particle

def wallHit3(x,y,x2,y2,angle,m,b,particle):
    # angle is between pi and 3pi/2, look at x2 and y2
    if x-x2 < y-y2:
        #it hits the x axis, new starting point is (x2,0)
        newX, newY = x2, 0
    else:
        #it hits the y axis, new starting point is (0,y2)
        newX, newY = 0, y2
    wallHit3Graphics(m,b,angle,x,y,particle)
    newAngle = 2*pi - angle
    newM = particleSlope(newAngle)
    newB = particleIntercept(newM, newX, newY)
    result = [newX, newY, newAngle, newM, newB]
    particle.left(newAngle)        
    return result   

def wallHit3Graphics(m,b,angle,x,y,particle):
    y_new = (m*0)+b
    angle_1 = (3*pi/2) - angle        
    if y_new < 0:
        h = y/cos(angle_1)
        particle.forward(abs(h))
    else:
        h = x/sin(angle_1)
        particle.forward(abs(h))
    return particle

def wallHit4(x,y,x2,y1,angle,m,b,particle):
    # angle > 3pi/2, look at x2 and y1
    if x-x2 < y-y1:
        #it hits the x axis, new starting point is (x2,0)
        newX, newY = x2, 0
    else:
        #it hits x=100, new starting point is (100,y1) 
        newX, newY = 100, y1
    wallHit4Graphics(m,b,angle,x,y,particle)
    newAngle = 2*pi - angle
    newM = particleSlope(newAngle)
    newB = particleIntercept(newM, newX, newY)
    result = [newX, newY, newAngle, newM, newB]
    particle.left(newAngle)        
    return result    

def wallHit4Graphics(m,b,angle,x,y,particle):
    y_new = (m*100)+b
    if y_new > 100:
        h = (100-y)/sin(angle)
        particle.forward(abs(h))
    else:
        h = (100-x)/cos(angle)
        particle.forward(abs(h))
    return particle
    

def main(trials):
    failure = 0
    success = 0
    wn = turtle.Screen()    
    particle = Graphics()
    buildContainer(wn,detectorCorner1)
    for i in range(trials):
        x,y = makeParticle()
        angle = particleDirection()
        m = particleSlope(angle)  
        b = particleIntercept(m,x,y)        
        particle = goTo(particle,x,y,angle)
        result = wallHit(x,y,angle,m,b,particle)
        if result == False:
            failure += 1
        if result == True:
            success += 1
    wn.exitonclick()
    efficiency = success / trials
    return efficiency