# Ethan Bennett
# This module tests integers for primality.
# An integer n is prime if if is evenly divided only by 1 and itself
# For instance 2, 3, 5, 7 are prime but 4 and 6 are not since 4 = 2*2 and 6 = 2*3
# You must implement a test. 

def isPrime(n):
    """
    Returns True or False according to whether n is prime.
    >>> isPrime(17)
    True
    >>> isPrime(18)
    False
    """
    '''check if integer n is a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True    

def main():
    print('Testing...')
    import doctest
    doctest.testmod()

if __name__=='__main__':
    main()
