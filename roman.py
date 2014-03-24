# Name: Ethan Bennett
# These functions convert to/from roman to indian/arabic numerals
# You can assume the following equivalences:
#   I 1    V 5    X 10    L 50    C 100    D 500    M 1000
# 

def toRoman(n):
    """
    This function converts positive integer n to its roman form.
    >>> toRoman(3)
    'III'
    >>> toRoman(1762)
    'MDCCLXII'
    """
    number = ''
    l=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    letter=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    for i in range(len(l)):
        while n >= l[i]:
            number = number + letter[i]*(n//l[i])                
            n = n-l[i]*(n//l[i])
    return number    

def fromRoman(s):
    """
    Converts string s, assumed to be a roman numeral to integer
    >>> fromRoman('III')
    3
    >>> fromRoman('MDCCLXII')
    1762
    """  
    number = 0
    s = list(s)
    for i in range(len(s)-1):      
        if s[i] == 'C' and s[i+1] == 'M':
            number = (number + 900) - 1100
        if s[i] == 'C' and s[i+1] == 'D':
            number = (number + 400) - 510
        if s[i] == 'X' and s[i+1] == 'C':
            number = (number + 90) - 110
        if s[i] == 'X' and s[i+1] == 'L':
            number = (number + 40) - 51
        if s[i] == 'I' and s[i+1] == 'X':
            number = (number + 9) - 11
        if s[i] == 'I' and s[i+1] == 'V':
            number = (number + 4) - 6
    for i in range(len(s)):      
        if s[i] == 'M':
            number = number + 1000
        if s[i] == 'D':
            number = number + 500
        if s[i] == 'C':
            number = number + 100
        if s[i] == 'L':
            number = number + 50
        if s[i] == 'X':
            number = number + 10
        if s[i] == 'V':
            number = number + 5
        if s[i] == 'I':
            number = number + 1
            
    return number

#
# The following are the standard way to ensure easy testing
#
def main():
    print('Testing...')
    import doctest
    doctest.testmod()

if __name__=='__main__':
    main()
    
