file = 'junk.txt'

def readInWords(file):
    occ = {}
    fh = open(file, 'r')
    for line in fh:
        words = line.split()
        for word in words:
            if word.endswith("'s"):
                word = word[:-2]
            word = word.lower().strip("';:,.!?-@#$%^&*()\][?><")
            if word not in occ:
                occ[word] = 0
            occ[word] += 1
    fh.close()
    return occ

def convert(occ):
    """returns of list of tiples (numberofocc,word)"""
    l = []
    for key,datum in occ.items():
        l.append([datum,key])
    return l

def main():
    l = convert(readInWords(file))
    l.sort(reverse=True)
    for u in range(4):
        print('{0:10d} {1:20s}'.format(l[u][0], l[u][1]))
main()