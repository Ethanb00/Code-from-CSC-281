lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
def zip(lst1,lst2):
    return [(lst1[i],lst2[i]) for i in range(min(len(lst1),len(lst2)))]

