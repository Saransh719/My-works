#28-09-2023
#C4
'''Write a menu driven program using which create a database beta and create 2 tables in it and run the following functions
Student-Admnno,Name,Year of passing, university number
University-University number,University name,Grading of university,Location,Country
1)Add a record      2)Delete a record      3)Update a record'''
import pymysql as p
con1=p.connect(host="localhost",user="root",passwd='')
cur1=con1.cursor()
cur1.execute("create database beta")
cur1.execute("use beta")
def Createtable():
    cur1.execute('''Create table University
(Uni_no int primary key,
Uname varchar(30),
Grading char(1),
Location varchar(30),
Country varchar(10)
)''')
    cur1.execute('''Create table student
(Admn_no int primary key,
Name varchar(30) not null,
Year_of_passing char(4),
Uno int
)''')
    cur1.execute("alter table student add foreign key (uno) references university(uni_no)")
def Addrecord():
    c=input("Enter table in which records are to be entered ")
    if c.lower()=='student':
        admno=int(input("Enter admission number "))
        name=input("Enter name of student ")
        yop=int(input("Enter year of passing "))
        uno=int(input("Enter university number "))
        cur1.execute("insert into student value({},'{}',{},{})".format(admno,name,yop,uno))
        con1.commit()
    elif c.lower()=='university':
        uno=int(input("Enter university number "))
        uname=input("Enter university name ")
        grade=input("Enter grade of university ")
        location=input("Enter location of university ")
        country=input("Enter country in which university is located ")
        cur1.execute("insert into university value({},'{}','{}','{}','{}')".format(uno,uname,grade,location,country))
        con1.commit()
    else:
        print("Enter valid table")
    print("Record added")     
def deleterecord():
    c=input("Enter table in which records are to be deleted ")
    if c.lower()=='student':
         admno=int(input("Enter admission number "))
         cur1.execute("delete from student where admn_no={}".format(admno))
         con1.commit()
    elif c.lower()=='university':
        uno=int(input("Enter university number "))
        cur1.execute("delete from university where uni_no={}".format(uno))
        con1.commit()
    else:
        print("Enter valid table")
    print("Record deleted")
def updaterecord():
    c=input("Enter table in which records are to be updated ")
    if c.lower()=='student':
        admno=int(input("Enter admission number of student to be updated "))
        name=input("Enter new name of student ")
        yop=int(input("Enter new year of passing "))
        uno=int(input("Enter new university number "))
        cur1.execute("update student set name='{}',year_of_passing='{}',uno={} where admn_no={}".format(name,yop,uno,admno))
    elif c.lower()=='university':
        uno=int(input("Enter university number to edit "))
        uname=input("Enter new university name ")
        grade=input("Enter new grade of university ")
        location=input("Enter new location of university ")
        country=input("Enter new country in which university is located ")
        cur1.execute("update university set uname='{}',grading='{}',location='{}',country='{}' where uni_no={}".format(uname,grade,location,country,uno))
    else:
        print("Enter valid table")
    con1.commit()
    print("Record updated")
Createtable()
while True:
    ans=input('''
1)Add a record
2)Delete a record
3)Update a record
''')
    if ans=='1':
        Addrecord()
    elif ans=='2':
        deleterecord()
    elif ans=='3':
        updaterecord()
    elif ans=='0':
        break
