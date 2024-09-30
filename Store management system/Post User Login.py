import pwinput
import pickle
#using pickle module to read the login information stored previously
with open("templogin.txt","rb") as f:
    L=pickle.load(f)
    logname=L[1]
    passwd=L[3]
    while True:
        try:
            user=int(input(f'''*************************************{logname}*************************************************
Enter 1 to login as employee(Password required)
Enter 2 to login as customer(No password required)
Enter 0 to exit
Enter your choice: '''))
            if user==1:
                password=pwinput.pwinput("Enter your password ")
                if password==passwd:
                    check="employee"
                    break
                else:
                    print("Wrong password")
            elif user==2:
                check="customer"
                break
            elif user==0:
                break
            else:
                print("Enter valid option")
        except ValueError:
            print("Enter valid option")