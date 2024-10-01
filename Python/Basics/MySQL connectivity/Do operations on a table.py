#22-09-2023
#C2
'''Write a menu driven program that reads a table emp and do the following tasks
1)Fetch and display all the record of a specific department and also display number of records in that department
2)Add a new record
3)Delete a record'''
import pymysql as p
con1=p.connect(host='localhost',user='root',passwd='',database="alpha")
cur1=con1.cursor()

def addnew():
        empid=int(input("enter emp id "))
        name=input("enter Name ")
        esal=int(input("enter Salary "))
        edept=input("enter Department ")
        q="insert into emp value({},'{}',{},'{}')".format(empid,name,esal,edept)
        cur1.execute(q)
        con1.commit()

def deleterecord(empid):
        cur1.execute("delete from emp where empno='{}'".format(empid))
        con1.commit()

def fetchdata(dept):
        cur1.execute("select * from emp where edept='{}'".format(dept))
        data=cur1.fetchall()
        count=len(data)
        for rec in data:
                print(rec[0],rec[1],rec[2],rec[3])
        print("No of records are",count)
        return
while True:
    ans=input('''
1)Fetch and display all the record of a specific department and also display number of records in that department
2)Add a new record
3)Delete a record
0)Exit
''')
    if ans=='1':
        fetchdata(input("Enter department "))
    elif ans=='2':
        addnew()
    elif ans=='3':
        deleterecord(int(input("Enter empid ")))
    elif ans=='0':
        break
