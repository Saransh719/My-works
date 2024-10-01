#04-05-2023
#R7
'''WAP to read a list L1 and another list L2 where L1 is in ascending order and L2 is in descending order. Merge the 2 list into L3 while sorting so that L3 is in descending order'''

def RL1():
    e=int(input("Enter no of elements for L1 "))
    L1=[int(input("element {} of L1 ".format(x+1))) for x in range(e)]
    L1.sort()
    return L1

def RL2():
    e=int(input("Enter no of elements for L2 "))
    L2=[int(input("element {} of L2 ".format(x+1))) for x in range(e)]
    L2.sort(reverse=True)
    return L2

def WL3():
    from bisect import insort
    L3=[]
    i=-1
    for x in L1:
        insort(L3,x, key=lambda L3: -1 * L3)
    for x in L2:
        insort(L3,x, key=lambda L3: -1 * L3)
    return(L3)

L1=RL1()
L2=RL2()
print("Your new list is",WL3())

