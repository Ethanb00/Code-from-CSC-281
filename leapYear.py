# Ethan Bennett
# This program is a leap year calculator
def leapYear(year):
    """
    A boolean function that returns True or False according to 
    whether year is a leap year.
    >>> leapYear(2001)
    False
    >>> leapYear(2004)
    True
    """
    return year//4 == year/4 and year//100 == year/100 and year//400 == year/400 or year// 4 == year/4 and year//100 != year/100




def leapYears(startYear, endYear):
    """
    This function returns a list of boolean values, one for each
    year from startYear to endYear (inclusive) indicating whether the
    year was a leap year.
    >>> leapYears(2001,2004)
    [False, False, False, True]
    """
    yearList = []
    for i in range(startYear, endYear+1):
        yearList.append(leapYear(i))
    return yearList


#
# The following are the standard way to ensure easy testing
#
def main():
    print('Testing...')
    import doctest
    doctest.testmod()
    print('End.')

if __name__=='__main__':
    main()
