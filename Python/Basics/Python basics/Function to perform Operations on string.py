#18-04-2023
#R2
'''Write a menu driven program to read a string from the user and perform folowing operations on the string by defining separate user defined functions  for each operation-:
a)Check whether string is palindrome(ignore case)(give bool value)
b)Replace a substring in a string and return changed string (precise case)
c)Capitalize the string
d)Toggle the string
e)Check the occurence of a subtring in a string. If found return position else return none
f)Return new string in title case
g)Status of string(Return tuple)
'''
from string import *
def PAL(a):
    a=a.lower()
    if a==a[::-1]:
        pal=True
    else:
        pal=False
    return pal

def REP(a):
    I=input("enter substring ")
    R=input("enter string to replace with ")
    a=a.replace(I,R)
    return a

def CAP(a):
    a=a.upper()
    return(a)

def TOG(a):
    a=a.swapcase()
    return a

def FIND(a):
    I=input("Enter substring to find ")
    T=a.find(I) + 1
    if T==0:
        return None
    else:
        return T

def TITLE(a):
    a=a.title()
    return a

def STATUS(a):
    v,c,d,u,l,sp,word=0,0,0,0,0,0,0,
    for x in a:
        if x in ascii_letters:
            if x in "aeiouAEIOU":
                v+=1
            else:
                c+=1
            if x.isupper()== True:
                u+=1
            elif x.islower()== True:
                l+=1
        elif x in digits:
            d+=1
        elif x in punctuation:
            sp+=1
    a=a.split()
    word=len(a)
    return (c,v,d,u,l,sp,word)
#__main__
while True:
    ans=input('''
1 to Check whether string is palindrome
2 to Replace a substring in a string and return changed string
3 to Capitalize the string
4 to Toggle the string
5 to Check the position of a subtring in a string.
6 to Return new string in title case
7 to Status of string
0 to exit
''')
    string=input("Enter your string ")
    if ans=='1':
        print(PAL(string))
    elif ans=='2':
        print(REP(string))
    elif ans=='3':
        print(CAP(string))
    elif ans=='4':
        print(TOG(string))
    elif ans=='5':
        print(FIND(string))
    elif ans=='6':
        print(TITLE(string))
    elif ans=='7':
        print("Status in order- consonant,vowel,digit,upper,lower,special character,no. of words is",STATUS(string))
    elif ans=='0':
        break
    else:
        print("Enter a valid options")
    
    
