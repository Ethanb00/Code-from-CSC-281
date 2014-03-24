'''

v = True
w = 1 > 2
r = 1 > 2 and 2 > 3 or 5 < 7
if 1>2 and 2>3 or 5<7:
    print('Yeah!')
else:
    print('Noooo!')

if 1>2:
    x=1
elif 2>3:
    x=2
elif 3<4:
    x=3
else:
    x=4
print(x)


()
**
* /
+ -
> < = ...
not 
and
or

'''


## Sentences := nounphrase verbphrase
## nounphrase := article adjective nouns
## article := one of [the, a, one]
## noun := one of [cat, bat, ball, dog, fly]
## verbphrase := verb nounphrase
## verb := one of [saw, hit, liked, caught, killed, painted]

## the cat painted the ball

from random import randint
articles = ['one', 'a', 'the']
nouns = ['cat', 'bat', 'ball', 'dog', 'fly', 'potato', 'banana', 'professor']
verbs = ['saw', 'hit', 'liked', 'caught', 'killed', 'painted', 'ate',]
adjectives = ['pretty', 'nice', 'sad', 'slippery', 'angry', 'clammy', 'fluffy']



def sentence():
    s = nounphrase() + ' ' + verbphrase()
    s = s.capitalize()+'.'
    return s

def nounphrase():
    s = article()+ ' ' + adjectiveStar() + ' ' + noun()
    return s

def adjectiveStar():
    s = ''
    for i in range(randint(0,3)):
        s = s + ' ' + adjective()
    return s

def verbphrase():
    s = verb() + ' ' + nounphrase()
    return s

def adjective():
    return randomThing(adjectives)    
    


def article():
    return randomThing(articles)

def randomThing(u):
    return u[randint(0,len(u)-1)]

def noun():
    return randomThing(nouns)

def verb():
    return randomThing(verbs)

def poem():
    verse = [] 
    for i in range(10):
        verse.append(sentence())
    return verse

def printPoem(verse):
    for v in verse:
        print(v)