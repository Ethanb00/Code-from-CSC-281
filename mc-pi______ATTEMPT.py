from math import sqrt,pi
from random import uniform

def getPoint():
    x=uniform(0,1)
    y=uniform(0,1)
    return(x,y)


    
        
    
def main():
    import doctest
    print("Testing...")
    doctest.testmod()

if __name__ == '__main__':
    main()
