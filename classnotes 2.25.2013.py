#def between1and10(n):
#    """
#    return true if n is betwen 1 and 10
#    """
#    return 1 <= n <= 10
#def between(a,b,n):
#    """
#    return true if n between a and b
#    """
#    return a <= n <= b or a >= n >= b

def between(a,b,u):
    """
    return true if u[i] between a and b for each element of the list u
    """
    result = True
    for e in u:
        if not a <= e <= b:
            result = result and False
    return result 