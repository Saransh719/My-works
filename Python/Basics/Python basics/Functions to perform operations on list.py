#20-8-2023
#R3
'''
Write a menu driven program to perform following functions on a linear list of 10 integers-:
a)Add an element in the beggining of the list
b)Add an element at the end of the list
c)Add an element to given position of the list
d)Remove and element from the beginning of the list
e)Remove an element from the end of the list
f)Tell the position of an element in the list
'''

def ADDBEG(l):
    l.insert(0,int(input("enter element to add ")))
    return(l)

def ADDEND(l):
    l.append(int(input("enter element to add ")))
    return(l)

def ADDPOS(l):
    p=int(input("enter position to add element at "))
    l.insert(p-1,int(input("enter element to add ")))
    return(l)

def REMBEG(l):
    l.pop(0)
    return(l)

def REMEND(l):
    l.pop()
    return(l)

def REMSEA(l):
    e=int(input("enter element to find "))
    i=1
    for y in l:
        if y==e:
            return(i)
            break
        else:
            i+=1
    else:
        return("element not found")
#__main__

l=[]
for x in range (10):
    l.append(int(input("Enter element ")))
print(l)
while True:
    ans=input('''
1 to Add an element in the beggining of the list
2 to Add an element at the end of the list
3 to Add an element to given position of the list
4 to Remove and element from the beginning of the list
5 to Remove an element from the end of the list
6 to Tell the position of an element in the list
0 to exit
''')
    if ans=='1':
        print(ADDBEG(l))
    elif ans=='2':
        print(ADDEND(l))
    elif ans=='3':
        print(ADDPOS(l))
    elif ans=='4':
        print(REMBEG(l))
    elif ans=='5':
        print(REMEND(l))
    elif ans=='6':
        print(REMSEA(l))
    elif ans=='0':
        break
    else:
        print("Enter a valid options")

    
    
