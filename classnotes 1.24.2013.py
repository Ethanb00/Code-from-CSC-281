#using defining functions to solve a volume question


def areaCircle(radius):
    area = 3.1415926 * radius * radius
    return area

def areaDonut(innerRadius, outerRadius):
    innerArea = areaCircle(innerRadius)
    outerArea = areaCircle(outerRadius)
    return outerArea - innerArea

def volumeCylinder(innerRadius, outerRadius, height):
    ad = areaDonut(innerRadius, outerRadius)
    v = ad * height
    return v

def main():
    r1 = input('innerRadius')
    r1 = float(r1)
    r2 = input('outerRadius')
    r2 = float(r2)
    h = input('height')
    h = float(h)
    a = volumeCylinder(r1,r2,h)
    print(a)
    
main()