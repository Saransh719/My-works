#28-09-2023
#C3
'''Consider 2 tables vehicle and chalaan in alpha database and create a menu driven program to perform the following operations-
a)Delete the records from chalaan table based on chalaan number and display all records
b)Increase the chalaan amount by 20% for all those who have data of chalaan before August 2022 and display all records
'''
import pymysql as p
con1=p.connect(host="localhost",user="root",passwd='',database='alpha')
cur1=con1.cursor()

def displayrecords():
    cur1.execute("select * from chalaan")
    print("Cno       Regno        Date of issue        Amount")
    print("---------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+"        "+str(rec[1])+"            "+str(rec[2])+"          "+str(rec[3]))

def Del(cno):
    cur1.execute(f"delete from chalaan where cno={cno}")
    displayrecords()

def increase():
    cur1.execute("update chalaan set amount=amount+amount*20/100 where DOChalaan<'2022-08-01'")
    displayrecords()
#__main__
while True:
    choice=int(input('''
Enter 1 to delete a chalaan
Enter 2 to increase the chalaan amount by 20% for all those who have data of chalaan before August 2022
Enter 3 to display all records
Enter 0 to exit '''))
    if choice==1:
        Del(int(input("Enter chalaan no of chalaan which you want to delete ")))
    elif choice==2:
        increase()
    elif choice==3:
        displayrecords()
    elif choice==0:
        break
    else:
        print("Enter a valid choice")



