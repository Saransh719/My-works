import pwinput
import pymysql as p
import pickle
#importing pickle module to read the user information
amountpurchased=[]
columnwidth=21
with open("templogin.txt","rb") as f:                 #Getting variables from login
    L=pickle.load(f)
    userid=L[0]
    logname=L[1]
con1=p.connect(host="localhost",user='root',passwd='',database="Project")  #Establishing sql connection
cur1=con1.cursor()
cur2=con1.cursor()
#buy function is used to buy items from a store
def buy():
    bought=False
    outofstockcheck={}   #Creating a dictionary of quantity of all items
    cur1.execute("select * from stock{}".format(userid))
    print("*********************************************************ITEMS AVAILABLE**************************************")
    print("Product id"+" "*(columnwidth-len("Product id")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("Price")),"Quantity")
    print("------------------------------------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
        outofstockcheck[rec[0]]=rec[4]    #Adding quantities to dictionary
    while True:
        try:
            print("-----------------------------------------------------------------------------")
            option=int(input('''BUYING OPTIONS
1)Add items to cart
2)Check cart
3)Check total amount
4)Purchase
5)Delete item from cart
0)Go back 
Enter your choice:'''))
            if option==1:
                while True:
                    prodchoice=int(input("Enter  Product id of product you want to purchase:"))
                    quantity=int(input("Enter quantity of product to buy:"))
                    try:    
                        if outofstockcheck[prodchoice]>quantity:
                            try:
                                cur1.execute("update stock{} set quantity=quantity-{} where sno={}".format(userid,quantity,prodchoice))
                                cur1.execute("insert into cart(select sno,name,company,price,{} from stock{} where sno={})".format(quantity,userid,prodchoice))
                                con1.commit()
                            except p.err.IntegrityError:           #To add same product again to increase quantity
                                cur1.execute("update stock{} set quantity=quantity-{} where sno={}".format(userid,quantity,prodchoice))
                                cur1.execute("update cart set quantity=quantity+{} where sno={}".format(quantity,prodchoice))
                                con1.commit()
                            print("Item added to cart")
                        else:
                            print("Out of stock")
                    except KeyError:
                        print("Enter valid Product id")
                    i=input("Press enter to add more")
                    if i!='':
                        break
            elif option==2:
                viewcart()
            elif option==3:
                print("Your total amount is",checktotal())
            elif option==4:
                purchase()
                bought=True
                break
            elif option==5:
                deletefromcart()
            elif option==0:
                cur1.execute("select * from cart")
                if bought==False and cur1.fetchall()!=None:                   #If customer did not buy, adding back to stock
                    cur1.execute("select * from cart")                                
                    for rec in cur1.fetchall():
                        cur1.execute("update stock{} set quantity=quantity+{} where sno={}".format(userid,rec[4],rec[0]))
                    cur1.execute("delete from cart")
                    con1.commit()
                break
        except ValueError:
            print("Enter valid option")
def deletefromcart():
    viewcart()
    deletechoice=int(input("Enter serial number of product which you want to remove"))
    cur1.execute("select quantity from cart where sno={}".format(deletechoice))
    cur1.execute("update stock{} set quantity=quantity+{} where sno={}".format(userid,cur1.fetchone()[0],deletechoice))
    cur1.execute("delete from cart where sno={}".format(deletechoice))
    con1.commit()
    print("Item removed from cart successfully")
def viewcart():
    amount=[]
    cur1.execute("select * from cart")
    cur2.execute("select price*quantity from cart")
    for rec in cur2:
        amount.append(rec[0])
    i=0
    print("*********************************************************CART***********************************************")
    print("Productid"+" "*(columnwidth-len("Productid")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("price")),"Quantity"+" "*(columnwidth-len("quantity")),"Amount")
    print("----------------------------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))),amount[i])
        i+=1
    print((" "*columnwidth*5)+"Total=",checktotal())
def checktotal():
    cur1.execute("select sum(price*quantity) from cart")
    return cur1.fetchone()[0]
def purchase():
    print("\nYour total amount is",checktotal())
    payment=int(input(''' PURCHASING OPTIONS
Enter 1 to pay via cash
Enter 2 to pay via upi
Enter your choice:'''))
    if payment==1:
        cash=float(input("Enter amount of cash given:"))
        if cash>=checktotal():
            print("Your change is",cash-checktotal())
            print("Thank you for Purchasing")
        else:
            print("Less amount given")
    if payment==2:
        upid=input("Enter upi id:")
        pin=pwinput.pwinput("Enter upi pin:")
        print("Thank you for purchasing")
    cur1.execute("insert into sales{} values(curdate(),{})".format(userid,checktotal()))
    cur1.execute("delete from cart")
    con1.commit()
def addtostock():
    cur1.execute("select * from stock")
    print("*********************************************************ITEMS AVAILABLE**************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Wholesale Price"+" "*(columnwidth-len("Wholesale price")),"Retail Price")
    print("------------------------------------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
    print("\n**********************************************************YOUR STOCK*******************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("Price")),"Quantity")
    print("------------------------------------------------------------------------------------------------------------------------")
    cur1.execute("Select * from stock{}".format(userid))
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
    while True:
        try:
            option=int(input('''BUYING OPTIONS
    1)Add items to stock
    2)Check stock
    3)Check total amount
    4)Purchase
    0)Go back
    Enter your choice:'''))
            if option==1:
                addinstock()
            elif option==2:
                checkstock()
            elif option==4:
                purchasestock()
                break
            elif option==3:
                stocktotal()
            elif option==0:
                if amountpurchased==[]:
                    i=input("You have not bought anything.Do your really want to go back(Y/N)")
                    if i in 'Yy':
                        break
                    if i in 'Nn':
                        pass
                    else:
                        print("Enter a valid choice")
                else:
                    print("Please pay for the products bought.")
            else:
                print("Enter a valid option")
        except ValueError:
            print("Enter a valid choice")
def viewstock():
    cur1.execute("select * from stock{}".format(userid))
    print("*********************************************************ITEMS AVAILABLE**************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("Price")),"Quantity")
    print("------------------------------------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
#lessquantprods function tells which item has quantity less than 10 and is needed to be ordered
def lessquantprods():
    itemsordered=False
    cur1.execute("select * from stock{}".format(userid))
    print("***************************************ITEMS TO BE ORDERED*******************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")))
    print("-----------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        if rec[3]<10:
            itemsordered=True
            print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))))
    if itemsordered==False:
        print("No items are to be ordered")
def monthlysales(month):
    cur1.execute("select sum(amount_sold) from sales{} where monthname(date)='{}';".format(userid,month))
    return cur1.fetchone()[0]
def yearlysales(year):
    cur1.execute("select sum(amount_sold) from sales{} where year(date)='{}';".format(userid,year))
    return cur1.fetchone()[0]
def monthlypurchase(month):
    cur1.execute("select sum(amount_purchased) from purchase{} where monthname(date)='{}';".format(userid,month))
    return cur1.fetchone()[0]
def yearlypurchase(year):
    cur1.execute("select sum(amount_sold) from purchase{} where year(date)='{}';".format(userid,year))
    return cur1.fetchone()[0]
def monthlyprofit(month):
    print("Profit of",month,"month is",monthlysales(month)-monthlypurchase(month))
def yearlyprofit(year):
    print("Profit of",year,"year is",yearlysales(year)-yearlypurchase(year))
def addinstock():
    global amountpurchased
    while True:
        add=int(input("Enter Serial number of item which you want to order: "))
        quantity=int(input("Enter Quantity of new item ordered: "))
        cur1.execute("select wholesale_price from stock where sno={}".format(add))
        amountpurchased.append(cur1.fetchone()[0]*quantity)
        try:
            cur1.execute("insert into stock{}(select sno,name,company,retail_price,{} from stock where sno={})".format(userid,quantity,add))
        except p.err.IntegrityError:           #To add same product again to increase quantity
            cur1.execute("update stock{} set quantity=quantity+{} where sno={}".format(userid,quantity,add))
        con1.commit()
        print("Item added to stock")
        i=input("Press enter to add more")
        if i!='':
            break
def checkstock():
    print("\n**********************************************************YOUR STOCK*******************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Quantity"+" "*(columnwidth-len("quantity")),"Price")
    print("------------------------------------------------------------------------------------------------------------------------")
    cur1.execute("Select * from stock{}".format(userid))
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
#purchasestock is used to purchase items from the wholesaler
def purchasestock():
    global amountpurchased
    amount=sum(amountpurchased)
    print("Your total amount is",amount)
    payment=int(input('''PURCHASE OPTIONS
Enter 1 to pay via cash
Enter 2 to pay via upi
Enter your choice:'''))
    if payment==1:
        cash=float(input("Enter amount of cash given:"))
        if cash>=amount:
            print("Your change is",cash-amount)
            print("Thank you for Purchasing")
        else:
            print("Less amount given")
    if payment==2:
        upid=input("Enter upi id:")
        pin=pwinput.pwinput("Enter upi pin:")
        print("Thank you for purchasing")
    cur1.execute("insert into purchase{} values(curdate(),{})".format(userid,amount))
    con1.commit()
    amountpurchased=[]
def dailysales():
    cur1.execute("select sum(amount_sold) from sales{} where date=curdate();".format(userid))
    return cur1.fetchone()[0]
#stocktotal tells the amount of items bought from wholesaler
def stocktotal():
    print("Your amount is",sum(amountpurchased))
#showstock shows the current stock of items of the user
def showstock():
    cur1.execute("select * from stock")
    print("*********************************************************ITEMS AVAILABLE**************************************")
    print("Sno"+" "*(columnwidth-len("sno")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Wholesale Price"+" "*(columnwidth-len("Wholesale price")),"Retail Price")
    print("------------------------------------------------------------------------------------------------------------------------")
    for rec in cur1.fetchall():
        print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
#addtomainstock adds an item to the main stock through which users can add it to their own stock
def addtomainstock():
    try:
        id=int(input("Enter product id:"))
        name=input("Enter product name:")
        company=input("Enter product company:")
        wholesale_price=float(input("Enter wholesale price:"))
        retail_price=float(input("Enter retail price:"))
        cur1.execute(f"insert into stock value({id},'{name}','{company}',{wholesale_price},{retail_price})")
        con1.commit()
        print("Item added to main stock")
    except ValueError:
        print("Enter valid input")
    except p.err.IntegrityError:
        print("Product id already exists")
#editstock is used to rectify any mistakes done while entering information about a product
def editstock(id):
        while True:
            validid=False
            cur1.execute("select sno from stock")       #Checking if given id is present in table
            for rec in cur1.fetchall():
                if rec[0]==id:
                    validid=True
            if validid==False:
                print("Enter valid id")
                break
            try:
                editchoice=int(input('''              OPTIONS
1)Edit name
2)Edit company
3)Edit Wholesale price
4)Edit retail price
0)Go back
Enter your choice:'''))
                if editchoice==1:
                    name=input("Enter new name of product:")
                    cur1.execute(f"update stock set name='{name}' where sno={id}")
                elif editchoice==2:
                    company=input("Enter new company of product:")
                    cur1.execute(f"update stock set company='{company}' where sno={id}")
                elif editchoice==3:
                    wholesale_price=input("Enter new Wholesale Price of product:")
                    cur1.execute(f"update stock set Wholesale_price={wholesale_price} where sno={id}")
                elif editchoice==4:
                    retail_price=input("Enter new retail price of product:")
                    cur1.execute(f"update stock set Retail_price={retail_price} where sno={id}")
                elif editchoice==0:
                    break
                else:
                    print("Enter a valid option")
                print("Edited")
            except ValueError:
                print("Enter a valid choice")
            con1.commit()       
#both companyemp and master are used to see products of a specific company
def companyemp():
    company=input("Enter company name for which you want to see products:")
    cur1.execute(f"select * from stock{userid} where company='{company}'")
    i=cur1.fetchall()
    if i!=():
        print("*********************************************************ITEMS AVAILABLE**************************************")
        print("Product id"+" "*(columnwidth-len("Product id")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("Price")),"Quantity")
        print("------------------------------------------------------------------------------------------------------------------------")
        for rec in i:
            print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
    else:
        print("No products found")
def companymaster():
    company=input("Enter company name for which you want to see products:")
    cur1.execute(f"select * from stock where company='{company}'")
    i=cur1.fetchall()
    if i!=():
        print("*********************************************************ITEMS AVAILABLE**************************************")
        print("Product id"+" "*(columnwidth-len("Product id")),"Name"+" "*(columnwidth-len("name")),"Company"+" "*(columnwidth-len("company")),"Price"+" "*(columnwidth-len("Price")),"Quantity")
        print("------------------------------------------------------------------------------------------------------------------------")
        for rec in i:
            print(str(rec[0])+" "*(columnwidth-len(str(rec[0]))),str(rec[1])+" "*(columnwidth-len(str(rec[1]))),str(rec[2])+" "*(columnwidth-len(str(rec[2]))),str(rec[3])+" "*(columnwidth-len(str(rec[3]))),str(rec[4])+" "*(columnwidth-len(str(rec[4]))))
    else:
        print("No products found")