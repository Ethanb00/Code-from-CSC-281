def costlymerge2(lst1,lst2):
    '''merge correctly two arleady sorted lists
    >>> merge 2([1,3,5,7], [2,4,6])
    [1,2,3,4,5,6,7]
    '''
    return sorted(lst1+lst2)

def shortcut(i,lst):
    if i < len(lst):
        return lst[i:]
    else:
        return []

def merge2(lst1,lst2):
    '''does the same,bust correctly, not costly.'''
    i1 = 0
    i2 = 0
    lst = []
    while i1<len(lst1) and i2<len(lst2):
        if lst1[i1] < lst2[i2]:
            lst.append(lst1[i1])
            i1 += 1
        else:
            lst.append(lst2[i2])
            i2 += 1
    lst.extend(shortcut(i1, lst1)+shortcut(i2, lst2))
        
    return lst
def mergei(lsts):
    '''merging all lists in lsts (Which are already sorted)
    >>>merge([[1,2,3,5,7],[1,3,4,7,8],[2,3,5]])
    [1,1,2,2,3,3,3,4,5,5,7,7,8]'''
    lst2 = []
    for i in range(len(lsts)):
        lst2 = merge2(lsts[i], lst2)
    return lst2

def merge(lsts):
    '''same but recursive'''
    if len(lsts) == 0:
        return []
    else:
        return merge2(lsts[0],merge(lsts[1:]))

def fib(n):
    '''fib(n) = 1 if n<=1
    else
    fib(n) = fib(n-1) + fib(n-2)
    '''
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def exp(x,n):
    '''
    x**n without using **
    n is a power of 2
    '''
    if n==1:
        return x
    else:
        y = exp(x,n/2)
        return y*y