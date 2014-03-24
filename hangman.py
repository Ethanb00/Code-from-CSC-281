#Ethan Bennett

def hangman(Computer,Length):
    from random import choice
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    attempts = []
    options = []
    tries = 20
    mydictionary = readInWords('american-english.txt')                            #make a dictionary
    if Computer == True:
        word = computerWordPick(Length,mydictionary)
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
    if Computer == False:
        tries = 20        
        disp = guessDisp(Length)                                                  #make a list of Length number of '_'
        makeAList(Length,mydictionary,options)                                    #make a list of possibilties
        while '_' in disp:
            guess = pick(attempts,alphabet)                                       #make a guess
            answer = compAsk(alphabet,attempts,mydictionary,guess)                #has human say if answer is yes or no
            wordCheck(mydictionary,Length,options,disp,guess,answer)              #removes impossibilties from options or saves possibilties
            if answer == False:
                tries -= 1
                print('I have',tries,'tries left') 
                if tries == 0:
                    print('I lose')
                    return None
            print(''.join(disp))
        print('I win')

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

def makeAList(Length,mydictionary,options):
    for word in mydictionary[Length]:
        options.append(word)    

def guessDisp(Length):
    dispView = ['_']*Length
    return dispView

def pick(attempts,alphabet):
    from random import choice
    guess = choice(alphabet)
    alphabet.remove(guess)
    attempts.append(guess)
    return guess

def compAsk(alphabet,attempts,mydictionary,guess):
    print('is',guess,'in your word (y/n)')
    if input() == 'y':
        return True     
    else:
        return False
        
def wordCheck(mydictionary,Length,options,disp,guess,answer):
    if answer == False:
        for word in range(len(options)):
            for letter in options[word]:
                if letter == guess:
                    options[word] = ' '
            while ' ' in options:
                options.remove(' ')
            return options
    if answer == True:
        confirmLoc(guess,disp,options)
        if input('does it occur more than once? (y/n)') == 'y':
            times = int(input('how many more times?'))
            for i in range(times):
                confirmLoc(guess,disp,options)
        else:    
            return options
        
def confirmLoc(guess,disp,options):
    l = int(input("what is it's position? (0,1,2,3...)"))    
    disp[l] = guess
    for word in range(len(options)):
        if options[word][l] is not guess:
            options[word] = ' '
            while ' ' in options:
                options.remove(' ')
                return options                    

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
    from random import choice    
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