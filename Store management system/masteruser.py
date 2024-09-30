import pymysql as p
con1=p.connect(host="localhost",user='root',passwd='',database="Project")  #Establishing sql connection
cur1=con1.cursor()
from Loginfunctions import deluser,viewallid
from Userfunctions import addtomainstock,showstock,editstock,companymaster
import pwinput
print("*************************MASTER USER LOGGED IN**********************")
while True:
    try:
        masteroptions=int(input('''             MENU
1)Add new items to stock
2)View all current item of main stock
3)Edit items from current stock
4)View product of a specific compnany
5)View userids and name of all users
6)Delete an account
0)Exit
Enter your choice:'''))
        if masteroptions==1:
            addtomainstock()
        elif masteroptions==2:
            showstock()
        elif masteroptions==3:
            showstock()
            try:
                id=int(input("Enter the product id which you want to edit:"))
            except ValueError:
                print("Enter valid id")
            editstock(id)
        elif masteroptions==4:
            companymaster()
        elif masteroptions==5:
            viewallid()
        elif masteroptions==6:
            storeid=input("Enter store id to delete :")
            cur1.execute(f"select pass from user where id={storeid}")
            i=cur1.fetchone()
            if i!=None:
                deluser(storeid,i[0])
            else:
                print("Enter valid id")
        elif masteroptions==0:
            break
        else:
            print("Enter a valid option")
    except ValueError:
            print("Enter a valid option")