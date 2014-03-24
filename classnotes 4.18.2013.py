#solving hangman well

def readInWords(filename):
    f = open(filename, encoding='utf-8')
    mydictionary = {}
    for word in f:
        word = word.lower().strip()
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

def hangman(Computer,Graphics,Length):
    mydict = readInWords('american-english.txt')
    if Computer:
        return Computer_chooses(Graphics,Length,mydict)
    else:
        return Human_chooses(Graphics,Length)

def pickWord(d,length):
    from random import choice
    return choice(d[length])

def update(word,mask,letter,guesses,tries):
    guesses.append(letter)
    good = False
    for i in range(len(word)):
        if word[i] == letter:
            mask[i] = letter
            good = True
    if not good:
        tries += 1
    return guesses,mask,tries

def display(mask,tries,limit,Graphics):
    mask = ''.join(mask)
    print(mask,tries,'/',limit)

def Computer_chooses(Graphics,Length,mydict):
    print('Hello, I am HAL. I will pick a word.')
    word = pickWord(mydict,Length)
    mask = ['_']*len(word)
    tries,limit,guesses = 0,10,[]
    while tries < limit and '_' in mask:
        letter = input('Letter please: ')
        if letter.isalpha() and len(letter)==1 and letter not in guesses:
            guesses,mask,tries = update(word,mask,letter,guesses,tries)
            display(mask,tries,limit,Graphics)
        else:
            print('stupid.  I said a letter, and not one you used before.')
    if tries < limit:
        print('You win.')
    else:
        print('I win, my word was:',word)

def updated(mask,letter,positions):
    for pos in positions[1:]:
        mask[int(pos)] = letter
    return mask
    
def pickLetter(guesses,mask,tries):
    for i in range(tries,26):
        letter = 'abdcefghijklmnopqrstuvwxyz'[i]
        if letter not in guesses:
            return letter

def Human_chooses(Graphics,Length):
    tries,limit = 0,10
    mask = ['_']*Length
    guesses = []
    while tries < limit and '_' in mask:
        letter = pickLetter(guesses,mask,tries)
        guesses.append(letter)
        display(mask,tries,limit,Graphics)
        print('my letter is: ',letter)
        YN = input('Y,p0,p1,p2,.../or anything else for NO').lower()
        if YN.startswith('y'):
            positions = YN.split(',')
            mask = updated(mask,letter,positions)
        else:
            tries += 1      
    if tries < limit:
        print('I win')
        return True
    else:
        print('You win.')
        return False 