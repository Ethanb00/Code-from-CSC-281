def c2f(x):
    f = x * 9 / 5 + 32
    return f

def main():
    c = float(input('celsius:'))
    f = c2f(c)
    print(c,f)

main()