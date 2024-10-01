#2-05-2023
#R6(a)
'''Write a program to create a ragged or regular 2D list of names from students as per user's choice.Store all names in uppercase'''

def CList(m,n):
    L=[]
    for x in range(m):
        Temp=[]
        for y in range(n):
            i=input("enter {} element of {} row ".format(y+1,x+1))
            Temp.append(i.upper())
        L.append(Temp)
    print("Your list is",L)

m=int(input("enter no of rows for 2d list "))
n=int(input("enter no of columns for 2d list "))
CList(m,n)