#Ethan Bennett
#This program does 2 things: 
    #1) it calculates a final class grade as an integer 
    #2) it will allow the user to determine their letter grade after determining their interger grade.

print('Hello user!  I am a final class grade calculator.')  
print('I will ask you a series of questions about your class scores.')
print('Using your answers, I will be able to determine your grades!') 
print('Amazing, right!') 
print('When answering my questions remember to input only the NUMBER grade not the letter grade.') 
z='Press enter to begin...'

input(z)
a='what is your midterm "0" score?'
b=input(a)
c='what is your midterm "1" score?'
d=input(c)
e='what is your final score?'
f=input(e)
g='what is your total project score?'
h=input(g)
b=int(b)
d=int(d)
f=int(f)
h=int(h)
i=((b*10)+(d*10)+(f*20)+(h*60)) / 100
i=int(i)
print('your grade for the year is', i,'%')
j='if you would like to know your letter grade, input your final score now'
k=input(j)
k=int(k)
l='A'
m='A-'
n='B+'
o='B'
p='B-'
q='C+'
r='C'
s='C-'
t='D'
u='F'
if (k >= 93) and (k <= 100):
    print(l)
if (k >= 90) and (k <= 92):
    print(m)
if (k >= 87) and (k <= 89):
    print(n)
if (k >= 83) and (k <= 86):
    print(o)
if (k >= 80) and (k <= 82):
    print(p)
if (k >=77) and (k <= 79):
    print(q)
if (k >= 73) and (k <= 76):
    print(r)
if (k >= 70) and (k <= 72):
    print(s)
if (k >= 69) and (k <= 60):
    print(t)
if (k >= 0) and (k <= 59):
    print(u,', Try harder next time!')

print('Thank you for using the final course grade calculator! I hope you did well!')