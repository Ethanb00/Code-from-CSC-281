from random import choice

def hangman(Computer,Length):
    if Computer == False:
        possibilities = []        
        print('pick a word that is',Length,'letters long')
        input('press any key when you are ready')
        G = readInWords('american-english.txt')
        pick1 = wordPossibilities(G,Length,possibilities)
        letterPick(possibilities)
    if Computer == True:
        G = readInWords('american-english.txt')
        word = computerWordPick(Length,G)
        word1 = word
        dispWord = []
        guesses = []
        tries = 0
        for i in range(Length):
            dispWord.append('_')
        while '_' in dispWord:
            tries += 1
            if tries == 20:
                print('you lose, my word was:',word1)
                return None            
            guess = computerAsksHuman(guesses)
            word = list(word)
            for letter in word:
                x = ComputerCheck(word,guess,dispWord,letter)      
            print(''.join(dispWord),' you have:',20-tries,'tries left')
        print('You Win')
                    
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

def wordPossibilities(mydictionary,Length,possibilities):
    possibilities += (mydictionary[Length])

def letterPick(possibilities):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pick1 = choice(alphabet)
    print('is',pick1,'in your word?')
    answer1 = str(input('(y/n)'))
    if answer1 == 'y':
        print('where is', pick1,'in your word?')
        l1 = int(input('(0,1,2,3...)'))
        for i in range(len(possibilities)):
            if possibilities[i][l1] is not l1:
                print(possibilities[i])
                
       
def computerWordPick(Length,mydictionary):
    word = choice(mydictionary[Length])
    return word

def computerAsksHuman(guesses):
    guess = input('What is your guess?')
    if guess in guesses:
        print('you already guessed,', guess,'try again.')
        computerAsksHuman(guesses)
    else:
        guesses.append(guess)
    return guess

def ComputerCheck(word,guess,dispWord,letter):
    if letter == guess:
        l = word.index(letter)
        word[l]=''
        for i in range(len(dispWord)):
            if i == l:
                dispWord[i] = guess        
    
def displayWord(x,dispWord,guess):
    for place in range(len(dispWord)):
        if place == x:
            return dispWord.append(guess)
        