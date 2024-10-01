#16-05-2023
#R11
#WAP to store record of 5 students having admission number,name,marks,class and section in a text file "Students.txt" and then display it

def STORE():
    F=open("Students.txt",'w')
    L=[]
    for i in range (1,6):
        no=input("enter admission number of {} student ".format(i))
        name=input("enter Name of {} student ".format(i))
        marks=input("enter marks of {} student ".format(i))
        cands=(input("enter class and section of {} student ".format(i)))
        print("------------------------------------------------------------")
        F.writelines([no+"\t",name+"\t",marks+"\t",cands+"\n"])

def READ():
    F=open("Students.txt",'r')
    s=F.read()
    print(s)


STORE()
READ()

