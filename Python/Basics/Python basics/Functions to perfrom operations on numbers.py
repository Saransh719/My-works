#25-4-2023
#R4
'''Write a menu driven program with the following tasks-:
a)Check wheter the given no is armstrong number or not.
b)Return a fibonacci series of n elements
c)Return Factorial
d)Power which returns m to the power n
e)Take a list and randomly returns an element
f)Return a floating point no in passed argurment
g)Return five different elements from 1 to 100
'''
import random

def Armstrong(no):
    no=str(no)
    s=0
    for i in no:
        s+=int(i)**3
    if s==int(no):
        r="Armstrong no"
    else:
        r="Not an armstrong number"
    return(r)

def Fibonacci(n):
    L=[0,1]
    for x in range(n-2):
        L.append(L[-1]+L[-2])
    return(L)

def Factorial(n):
    fact=1
    for x in range(1,n+1):
        fact*=x
    return(fact)

def POW(m,n):
    return(m**n)

def Lreturn(L):
    return("The random element is",random.choice(L))

def Freturn(i,f):
    return(random.uniform(i,f))

def Dreturn():
    L=[x for x in range(1,101)]
    return(random.choices(L,k=5))

#__main__
try:
    while True:
        ans=int(input('''
Enter 1 to Check wheter the a no is armstrong number or not
Enter 2 to Get a fibonacci series of n elements
Enter 3 to Get Factorial of a number
Enter 4 to Get m to the power n
Enter 5 to Get any random element of list
Enter 6 to Get a floating point no in passed range
Enter 7 to Get five different elements from 1 to 100
Enter 0 to exit
'''))
        if ans==1:
            print(Armstrong(int(input("enter number "))))
        elif ans==2:
            print(Fibonacci(int(input("enter number of elements "))))
        elif ans==3:
            print(Factorial(int(input("enter number "))))
        elif ans==4:
            print(POW(int(input("enter base ")),int(input("enter power "))))
        elif ans==5:
            e=int(input("no of elements "))
            L=[int(input("element ")) for x in range(e)]
            print("This is your list",L)
            print(Lreturn(L))
        elif ans==6:
            print(Freturn(int(input("enter initial value ")),int(input("enter final value "))))
        elif ans==7:
            print(Dreturn())
        elif ans==0:
            print("exitiing.......")
            break
        else:
            print("Enter a valid argument")
except ValueError:
    print("Enter a valid argument")
        


