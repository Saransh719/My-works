#24-08-2023
#R20
#Write a progream to reverse a String using a Stack

def reversestring(string):
    stack=[]
    for x in string:
        stack.append(x)
    s=''
    while stack:
        s+=stack.pop()
    return s

string=input("Enter string to be reversed ")
print("New string is",reversestring(string))
