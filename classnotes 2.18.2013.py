#def f(n):
#    print('X',n) #nonfruitful function
#a = f
#>>>a()
#from math import sqrt

#def f(n):
#    return sqrt(n)
#def g(n):
#    return 2*f(n) # this is a fruitful function
import turtle


def attendees(ticketPrice):
    """returns the number of attendees for a given price"""
    m = -15/0.10
    att = m * ticketPrice + 870
    return att

def variable(ticketPrice):
    """returns the variable cost given a price """
    att = attendees(ticketPrice)
    cost = 0.04 * att
    return cost

def cost(ticketPrice):
    """returns the total cost given a cost"""
    var = variable(ticketPrice)
    total = 180 + var
    return total

def revenue(ticketPrice):
    """returns the revenue"""
    att = attendees(ticketPrice)
    rev = ticketPrice * att
    return rev

def profit(ticketPrice):
    """returns the profit"""
    rev = revenue(ticketPrice)
    total = cost(ticketPrice)
    TP = rev - total
    return TP

def newGraphics():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.speed(0)
    alex.penup()
    alex.forward(-400)
    alex.pendown()
    return alex,wn

def endGraphics(wn):
    wn.exitonclick()

def barchart(alex,ticketPrices,profits):
    for i in range(len(ticketPrices)):
        height = profits[i]/10
        alex.left(90)
        alex.forward(height)
        alex.right(90)
        alex.write(ticketPrices[i])
        alex.forward(20)
        alex.right(90)
        alex.forward(height)
        alex.left(90)
             
def main():
    maxprofit = 0
    ticketPrices = []
    profits = []
    for i in range(200,610,10):
        ticketPrice = i / 100
        p = profit(ticketPrice)
        ticketPrices.append(ticketPrice)
        profits.append(p)
        if p >= maxprofit:
            maxprofit = p
            optprice = ticketPrice
    t,w = newGraphics()
    barchart(t,ticketPrices,profits)
    endGraphics(w)
    print('The best price is', optprice)
    print('You will make', maxprofit, 'dollars')
    return optprice, maxprofit