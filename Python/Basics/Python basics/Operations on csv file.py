#26-05-2023
#R15
'''WAP menu driven program to consider file 'Emp.csv' as [empid,name,salary,department,designation] and perform following operations
a)Add a record
b)Display a record of specific empid or name
c)Delete a record
d)Update a record
f)Display all records
'''
import csv
def ADD():
    with open("emp.csv",'a+',newline='') as F:
        flag=True
        WOB=csv.writer(F)
        ROB=csv.reader(F)
        empid=input("Enter Emp id ")
        F.seek(0)
        for rec in ROB:
          if rec[0]==empid:
                flag=False
        if flag==True:   
            name=input("Enter name ")
            salary=input("Enter salary ")
            department=input("Enter department ")
            designation=input("Enter Designation ")
            WOB.writerow([empid,name,salary,department,designation])
        else:
            print("Empid already present")
def Dall():
    with open("emp.csv",'r') as F:
        ROB=csv.reader(F)
        for Rec in ROB:
            print(Rec)

def DidOrname(ion):
    ion=str(ion).lower()
    with open("emp.csv",'r') as F:
        ROB=csv.reader(F)
        flag=True
        for Rec in ROB:
            if Rec[0].lower()==str(ion) or Rec[1].lower()==str(ion):
                print(Rec)
                flag=False
        if flag==True:
                print("Not found")

def Delete(i):
    L=[]
    i=str(i)
    with open("emp.csv",'r') as F:
        ROB=csv.reader(F)
        flag=False
        for Rec in ROB:
            if Rec[0]==str(i):
                flag=True
            else:
                L.append(Rec)
    if flag==True:
        with open("emp.csv",'w',newline='') as F:
            WOB=csv.writer(F)
            WOB.writerows(L)
    else:
        print("Record not found")

def Update(i):
    L=[]
    i=str(i)
    with open("emp.csv",'r+') as F:
        ROB=csv.reader(F)
        WOB=csv.writer(F)
        flag=False
        for Rec in ROB:
            if Rec[0]==str(i):
                name=input("Enter new name ")
                salary=input("Enter new salary ")
                department=input("Enter new department ")
                designation=input("Enter new Designation ")
                L.append([i,name,salary,department,designation])
                flag=True
            else:
                L.append(Rec)
    if flag==True:
        with open("emp.csv",'w',newline='') as F:
            WOB=csv.writer(F)
            WOB.writerows(L)
    else:
        print("Record not found")
            
#__main__
try:
    while True:
        ans=int(input('''
0 to Exit
1 to Add a record
2 to Display a record of specific empid or name
3 to Delete a record
4 to Update a record
5 to Display all records
'''))
        if ans==1:
            ADD()
        elif ans==2:
            DidOrname(input("Enter empid or name of employee to display"))
        elif ans==3:
            Delete(input("Enter empid of employee to delete"))
        elif ans==4:
            Update(input("Enter empid of employee to update"))
        elif ans==5:
            Dall()
        elif ans==0:
            print("exitiing.......")
            break
        else:
            print("Enter a valid argument")
except ValueError:
    print("Enter a valid argument")