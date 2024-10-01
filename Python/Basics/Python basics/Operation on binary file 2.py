#18-05-2023
#R13
'''Write a menu driven program to do the following operations on a binary file 'lib.dat'. The records in this file are in the follwing format
{'Bookid':___,'bname':___,'bprice':___,'bauthor':___,'bpub':__}
1)Add a record
2)Display booknames and id of a particular publisher
3)Display booknames and no of books written by a given author
4)Display the booknames with highest price
'''
import pickle
L=[]
def ADD():
    F=open("lib.dat",'ab')
    while True:
        Bookid=int(input("Enter Book id "))
        bname=input("Enter Book Name ")
        bprice=float(input("Enter Price "))
        bauthor=input("Enter name of author ")
        bpub=input("Enter Publisher name ")
        D={'Bookid':Bookid,'bname':bname,'bprice':bprice,'bauthor':bauthor,'bpub':bpub}
        pickle.dump(D,F)
        ch=input("Press enter to add more")
        if ch!="":
            break
    F.close()
    
    global L     #Making a list of file for later use
    F=open("lib.dat",'rb')
    try:
        while True:
            L.append(pickle.load(F))
    except EOFError:
        F.close()

def fpub(pub):
    global L
    for x in L:
        if x["bpub"].lower()==str(pub).lower():
            print("Book id-",x["Bookid"],"\nBook name-",x["bname"],"\n")

def fauth(auth):
    global L
    c=0
    for x in L:
        if x["bauthor"].lower()==str(auth).lower():
            c+=1
            print("Book name-",x["bname"])
    print("Total books written by author are",c)

def hprice():
    global L
    high=0
    for x in L:
        if x["bprice"]>high:
            high=x["bprice"]
    for x in L:
        if x["bprice"]==high:
            print("Name of books with highest price are-")
            print(x["bname"])

#__main__
try:
    while True:
        ans=int(input('''
0 to exit
1 to Add a record
2 to Display booknames and id of a particular publisher
3 to Display booknames and no of books written by a given author
4 to Display the booknames with highest price
'''))
        if ans==1:
            ADD()
        elif ans==2:
            fpub(input("Enter publisher "))
        elif ans==3:
            fauth(input("Enter author "))
        elif ans==4:
            hprice()
        elif ans==0:
            print("exitiing.......")
            break
        else:
            print("Enter a valid argument")
except ValueError:
    print("Enter a valid argument")
