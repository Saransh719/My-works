import pickle
import os
#os module is used to change the directory as shell seems to default to C:\Systen32
#os.chdir("")      
with open("User login.py") as f:      #Running the user login script
    exec(f.read()) 
with open("templogin.txt","rb") as f:
    userid=int(pickle.load(f)[0])
if userchoice!=0:
    if userid!=100:
        with open("post user login.py") as f:      #Running the customer/employee login script
            exec(f.read())     
        if check=="customer":
            with open("customer.py") as f:      #Running the Customer usage script
                exec(f.read())
        elif check=="employee":
            with open("employee.py") as f:
                exec(f.read())                  #Running the employee usage script
    elif userid==100:
        with open("masteruser.py") as f:
                exec(f.read())
