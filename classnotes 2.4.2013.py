#import math 
#i = math.sqrt(4) 
#print(i)

#from math import sqrt
#sqrt(4)

#from random import randint, uniform
#randint(1,10)  #includes both 1 and 10
#uniform(1,5) #random floats between 1 and 5

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key      = 'qwertyuiopasdfghjklzxcvbnm'


def cipher(message):
    #will return encypted version of message
    #for example if message is hello, returns 'itssg'
    # >>> cipher('hello') 
    # 'itssg'
    encrypted = ''
    for i in range(len(message)):
        for position in range(len(alphabet)):
            if message[i] == alphabet[position]:   #two equal signs test for equality
                encrypted = encrypted + key[position]
                
    return encrypted
    
message = input('Give me a message')
e = cipher(message)
print(e)