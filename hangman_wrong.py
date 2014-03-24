#Ethan Bennett
import random


#Change the mydictionary into a dictionary data structure


def hangman(Computer, Graphic, Length):  
   """
   I DON'T HAVE TO DO GRAPHICS
   This function starts a game where the computer is choosing the word     
   if Computer is True and you choose the word if Computer is False.     
   The words with be of length length     
   Graphics is either True or False and indicates whether the man is drawn.     
   It returns True if the computer wins and False if the computer Looses.     
   """
   if Computer == True:
      tries = 0
      word = '_'*Length      
      print("Hello, let's play hangman!\nI'm choosing a word... thinking...\nOk.")
      MakeMyDictionary('american-english.txt')      
      ComputerGuess(computerWordPick(Length),tries,Length,word)
   if Computer == False:
      tries = 0    
      word = '_'*Length      
      print('You are going to pick this time!\nOnce you have a word that is',Length,'letters long, hit any key')
      input('...')
      MakeMyDictionary('american-english.txt')  
      alphabet = 'abcdefghijklmnopqrstuvwxyz'      
      humanWordPick(tries,Length, word,alphabet)
   if Graphic == True:
      turtleDrawing()
 
def MakeMyDictionary(filename):
   '''This function cleans up and makes a list of strings with all the possible words for the computer to choose from'''
   f = open(filename, encoding='utf-8')
   mydictionary = []
   for word in f:
      word = word.strip()
      if word.endswith("'s"):
         word = word[:-2]
      else:
         words = []
      mydictionary.append(word)
   f.close()
   return mydictionary

def computerWordPick(Length):
   """ This fuction has the computer pick the word for the game"""
   for word in MakeMyDictionary('american-english.txt'):
      pick = random.choice(MakeMyDictionary('american-english.txt'))
      pickLength = len(pick) 
      if pickLength != Length:
         pick
      else:
         return pick

def ComputerGuess(pick,tries,Length,word):
   '''Computer asks for a guess from the human and confirm or deny its presence in the word'''
   print('here is my word so far')
   print(word)
   print(pick)
   Guess = input('What is your guess?')
   if '_' in word:
      if Guess in pick:
         print('yes!',Guess,'is in my word')
         for letters in pick:
            if Guess == letters:
               l = pick.index(letters)
               word = list(word)
               word[l] = Guess
               word = ''.join(word)
               x = repeatedLetter1(Guess,word)                
               print(word)
               ComputerGuess(pick,tries,Length,word)
      else:
         print(Guess,'is not in my word. Try again')
         ComputerGuess(pick,tries,Length,word)
   else:
      print('Wow!, you win!')
         
def repeatedLetter1(Guess,word): 
   
   word = list(word)
   word[l] = Guess
   word = ''.join(word)
   print(word)
   repeatedLetter(Guess,word)
   return word   

def humanWordPick(tries, Length, word,alphabet):
   '''Problem: will ask about letters multiple times'''
   if '_' in word:
      Guess = random.choice(alphabet)
      alphabet = alphabet.replace(Guess,'')
      if tries <= 20:
         print('Is', Guess,'in your word? (Y/N)')      
         if input() == 'Y':
            l = input('What letter of the word is it? (0,1,2,3...)')
            l = int(l)
            word = list(word)
            word[l] = Guess
            word = ''.join(word)
            print(word)            
            x = repeatedLetter(Guess,word) 
            print(x)
            print('Good!')
            humanWordPick(tries,Length, word,alphabet)
         else:
            tries += 1
            print('Ok,',tries,'/20')      
            humanWordPick(tries,Length,word,alphabet)
      else:
         print("'You win! I couldn't guess your word!")
   else:
      print('I win!')

def repeatedLetter(Guess,word):
   if input('Does it occur again? (Y/N)') == 'Y':
      l1 = input('What letter of the word is it? (0,1,2,3...)')
      l1 = int(l1)
      word = list(word)
      word[l1] = Guess
      word = ''.join(word)
      print(word)
      repeatedLetter(Guess,word)
      return word