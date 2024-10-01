#01-05-2023
#R5
'''WAP to consider a sorted list and create function which takes sorted list and new element as argument and inserts the new element in the sorted list at the correct position in the sorted list'''
def NOBISECT(L,E):
    i=0
    for x in L:
        if x>E:
            L.insert(i,E)
            break
        i+=1
    print("New sorted list is",L)
    print("-----------------------------")

def BISECT(L,E):
    from bisect import insort
    insort(L,E)
    print("New sorted list is",L)
    print("-----------------------------")

ne=int(input("no of elements for the list "))
L=[int(input("element ")) for x in range(ne)]
L.sort()
print("Initial sorted list is",L)
while True:
    e=int(input("enter element to add "))
    ans=input('''Enter 1 to not use bisect method
Enter 2 to use bisect method
Enter 0 to exit ''')
    if ans=='1':
        NOBISECT(L,e)
    elif ans=='2':
        BISECT(L,e)
    elif ans=='0':
        break
    else:
        print("Enter valid argument")
