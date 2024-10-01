#09-08-2023
#R17
#Write a complete menu driven program to implement stack operation on a list
top=None
def push(l,ele):
    global top
    l.append(ele)
    top=len(l)-1
def pop(l):
    global top
    if l==[]:
        print("Stack underflow")
    else:
        print(l.pop())
        top=len(l)-1
def peek(l):
    global top
    if l==[]:
        print("Stack underflow")
    else:
        print("Top element is",l[top])
def display(l):
    print("Your stack is ")
    if l==[]:
        print("Stack underflow")
    else:
        for x in l[::-1]:
            print(x)
l=[]
while True:
        ans=input('''
0 to exit
a to Push a record
b to Pop a record
c to See peak of stack
d to Display whole stack
''')
        if ans.lower()=='a':
            push(l,input("Enter element to enter "))
        elif ans.lower()=='b':
            pop(l)
        elif ans.lower()=='c':
            peek(l)
        elif ans.lower()=='d':
            display(l)
        elif ans=='0':
            print("exitiing.......")
            break
        else:
            print("Enter a valid argument")
