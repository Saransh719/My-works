from Userfunctions import *
print("****************************CUSTOMER LOGGED IN************************************")
while True:
        try:
                options=int(input('''     OPTIONS
1)Buy
0)Exit 
Enter your choice: '''))
                if options==1:
                      buy()
                elif options==0:
                    break
                else:
                      print("Enter a valid option")
        except ValueError:
              print("Enter a valid option")