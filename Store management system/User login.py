from Loginfunctions import *
import pickle
print('''**********************************************************STORE MANAGEMENT**************************************
                                                            BY: SARANSH SAPRA''')
while True:
    try:
        userchoice=int(input('''MAIN MENU
1)Login as existing user
2)Create new user
3)Delete existing user
0)Exit
Enter your choice: '''))
        if userchoice==1:
            loginuser()
            with open("userfoundcheck.txt","rb") as f:
                userfound=pickle.load(f)
            if userfound==True:
                break
        elif userchoice==2:
            adduser()
        elif userchoice==3:
            storeid=input("Enter store id to delete :")
            storepass=pwinput.pwinput("Enter your store password:")
            deluser(storeid,storepass)
        elif userchoice==0:
            break
        else:
            print("Enter valid option")
    except ValueError:
        print("Enter valid option")
