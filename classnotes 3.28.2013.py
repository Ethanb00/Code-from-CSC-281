def readInWords(filename):
    f = open(filename, encoding='utf-8')
    mydictionary = {}
    for word in f:
        word = word.strip().lower()
        if word.endswith("'s"):
            word = word[:-2]
        if word not in mydictionary:
            l = len(word)
            mydictionary[word] = len(word)
            if l in mydictionary:
                words = mydictionary[l]
            else:
                words = []
            words.append(word)
            mydictionary[l] = words
    f.close()
    return mydictionary

def solveCrossword(cw,mydictionary):
    '''
    solveCrossword((['af?', 'r??', '???])
    '''
    potential = []
    for row in cw:
        allwords = generateWords(row,mydictionary)
        potential.append(allwords)
    for answer in combine(potential):
        if vertcheck(answer,mydictionary):
            return answer  #crossword solved.
    return False        

def combine(uu):
    '''Returns a list of all combinations of elements of each lists of uu
    >>>combine([[1,2,3].[4,5]])
    [[1,4],[1,5],[2,4],[2,5],[3,4],[3,5]]
    '''
    u  = uu[0]
    r = []
    if len(uu) == 1:
        for e in uu[0]:
            r.append([e])
        return r
    for e in u:
        combinations = combine(uu[1:])
        for comb in combinations:
            r.append([e]+comb)
    return r

def vertcheck(words,mydictionary):
    '''
    checking that the columns of words are are in my dictionary
    vertcheck(['as', 'to'])
    True
    '''
    for column in range(len(words[0])):
        verticleWord = ''
        for word in words:
            verticleWord += word[column]
        if verticleWord not in mydictionary:
            return False
    return True

def generateWords(row,mydictionary):
    '''
    'af?' -> ['afa', 'afb', 'afc',...]
    '''
    words = []
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    if '?' in row:
        for letter in alphabet:
            words.extend(generateWords(row.replace('?', letter,1), mydictionary))
    else:
        if row in mydictionary:
            words = [row]
    return words

def main():
    G = readInWords('american-english.txt')
    solution = solveCrossword(['a??', '?a?', '??e'],G)
    for word in solution:
        print(word)

main()