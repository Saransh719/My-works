import pickle
#importing pickle to store login information
import pwinput
import pymysql as p
con1=p.connect(host="localhost",user='root',passwd='',database="Project")  #Establishing sql connection
cur1=con1.cursor()
#adduser function is used to add a new user to the data
def adduser():
    storename=input("Enter store name:")
    storepass=pwinput.pwinput("Enter your store password:")
    check=pwinput.pwinput("Confirm your store password:")
    while storepass!=check:
        print("Passwords do not match")
        storepass=pwinput.pwinput("Enter your store password:")
        check=pwinput.pwinput("Confirm your store password")
    epass=pwinput.pwinput("Enter employee password:")
    check=pwinput.pwinput("Confirm your employee password:")
    while epass!=check:
        print("Passwords do not match")
        epass=pwinput.pwinput("Enter employee password:")
        check=pwinput.pwinput("Confirm your employee password:")
    cur1.execute("insert into user(store_name,pass,epass) values('{}','{}','{}')".format(storename,storepass,epass))
    print("-------------------------------------------------------------------------------------")
    print("New user created")
    con1.commit()
    cur1.execute("select id from user where store_name='{}' and pass='{}' and epass='{}'".format(storename,storepass,epass))
    storeid=cur1.fetchone()[0]
    cur1.execute("create table stock{}(sno int primary key,name varchar(30) not null,company varchar(20),price float,quantity int)".format(storeid))
    cur1.execute("create table Purchase{}(date date,amount_purchased float)".format(storeid))
    cur1.execute("create table Sales{}(date date,amount_sold float)".format(storeid))
    print("Stock Info created")
    print("Purchase Info created")
    print("Sales Info created")
    print("---------------------------------------------------------------------------------------------")
    con1.commit()
    print("Your User id is",storeid,"\nPlease Remember it")
    print("**********************************************************************************************")

def loginuser():
    wrongpassword=True
    login=False
    storeid=int(input("Enter store id:"))
    while True:
        storepass=pwinput.pwinput("Enter your store password:")
        cur1.execute("select pass from user where id={}".format(storeid))
        try:
            passcheck=cur1.fetchone()[0]
            validid=True
        except TypeError:
            print("User not found")
            validid=False
        print("----------------------------------------------------------------------------------")
        if validid==True:         
            if storepass==passcheck:
                login=True
                cur1.execute("Select store_name from user where id={}".format(storeid))
                logname=cur1.fetchone()[0]
                print("Logged in as",logname)
                userid=storeid
                with open("templogin.txt","wb") as f:
                    cur1.execute("select epass from user where id={}".format(storeid))
                    pickle.dump([userid,logname,storepass,cur1.fetchone()[0]],f)
                with open("userfoundcheck.txt","wb") as f:
                    pickle.dump(validid,f)
                break
            else:
                print("Wrong password")
def deluser(storeid,storepass):
    cur1.execute("select pass from user where id={}".format(storeid))
    try:
        if storepass==cur1.fetchone()[0]:
            i=input("Do you really want to delete this store(Y/N)")
            if i in 'Yy':
                cur1.execute("delete from user where id={}".format(storeid))
                cur1.execute("drop table stock{},sales{},purchase{}".format(storeid,storeid,storeid))
                con1.commit()
                print("All records of store deleted successfully")
            elif i in 'Nn':
                pass
            else:
                print("Please enter either Y or N")
        else:
            print("Wrong password")
    except TypeError:
        print("Enter valid id")
#viewallid function is used to view the id and name of all users created
def viewallid():
    columnwidth=5
    cur1.execute("select id,store_name from user")
    print("*********************************************************USERS**************************************")
    print("ID"+" "*(columnwidth-len("ID")),"Store Name")
    print("--------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1]))