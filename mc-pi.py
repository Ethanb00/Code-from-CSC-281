#
# A Monte-Carlo Simulation to estimate pi
#
# Serge Kruk
# 2011.09.08
#
from math import sqrt,pi
from random import uniform


def getPoint():
    """
    Returns a random point in first quandrant.
    >>> (x,y)=getPoint()
    >>> x*x <= 1 and y*y <= 1 
    True
    """
    x=uniform(0,1)
    y=uniform(0,1)
    return (x,y)

def withinCircle(x,y):
    """
    Determine whether the point (x,y) is within the unit circle
    centered at (0,0). We do this by checking that sqrt(x^2+y^2) <= 1
    >>> withinCircle(0.5,0.5)
    True
    >>> withinCircle(1,0.5)
    False
    """ 
    if sqrt(x*x+y*y) <= 1:
        return True
    else:
        return False    


def approxPi(iterations,verbose):
    """
    This function accepts a number which will be the number of iterations
    to run.  And it returns its approximation of pi obtained after that
    number of iteration.
    The second parameters (verbose) indicates whether to print something 
    during the simulation.
    The following test ensures that the function returns an acceptable
    approximation.
    """
    As=0
    Ac=0
    for i in range(iterations):
        x,y=getPoint()
        if withinCircle(x,y):
            a='Hit'
            Ac=Ac+1
        else:
            a='Miss'
        p=(Ac/iterations)*4
        if verbose == True:
            print(i,x,y,a,p)
    return p
    
              

def main():
    import doctest
    print("Testing...")
    doctest.testmod()

if __name__ == '__main__':
    main()

