#17-05-2023
#R12
'''WAP to keep on adding records to a binary file 'prod.dat' the data stored as {'PID':___,'Pname':___,'Price':___,'Quantity':___,'Manufacturer':__}
a)Display the names of products of LG company
b)Display the names of those products which have quantity less than 10 in the stock
c)Display PID and name of theose products which have higest price in the stock
'''
import pickle

L=[]
def ADD():
    F=open("prod.dat",'ab')
    i=0
    while True:
        i+=1
        PID=int(input("Enter PID of product "))
        Pname=input("Enter Name of product ")
        Price=float(input("Enter Price of product "))
        Quantity=int(input("Enter Quantity of product "))
        Manufacturer=input("Enter Manufacturer name of product ")
        D={'PID':PID,'Pname':Pname,'Price':Price,'Quantity':Quantity,'Manufacturer':Manufacturer}
        pickle.dump(D,F)
        ch=input("Press enter to add more")
        if ch!="":
            break
    F.close()

def READ():
    F=open("prod.dat",'rb')
    print("Your file is:")
    try:
        while True:
            print(pickle.load(F))
    except EOFError:
        F.close()

def CREATELIST():
     global L
     F=open("prod.dat",'rb')
     try:
        while True:
            L.append(pickle.load(F))
     except EOFError:
        F.close()

def DISPLAYLG():
    global L
    print("Products with manufacturer LG are:")
    for x in L:
        if x['Manufacturer'].lower()=="lg":
            print(x['Pname'])
def QUANTITYLESS10():
    global L
    print("Products with quantity less than 10 are:")
    for x in L:
        if x['Quantity']<10:
            print(x['Pname'])
def HIGHESTVALUE():
    global L
    print("Products with maximum price are:")
    t=[]
    for x in L:
        t.append(x['Price'])
    for x in L:
        if x['Price']==max(t):
            print(x['PID'],'\t',x['Pname'])
ADD()
READ()
CREATELIST()
DISPLAYLG()    
QUANTITYLESS10()
HIGHESTVALUE()


