from calendar import month_name
#importing month name from calender module so that abbreviations of months can be used
from Userfunctions import *
print("****************************EMPLOYEE LOGGED IN************************************")
while True:
        try:
            options=int(input('''        OPTIONS
1)Buy
2)View stock
3)Add items to stock
4)See products which need to be ordered as soon as possible
5)Get monthly sales
6)Get yearly sales
7)Get monthly purchase
8)Get yearly purchase
9)Get monthly profit
10)Get yearly profit
11)Get today's sales
12)View products of a specific company
0) Exit
Enter your choice: '''))
            if options==1:
                buy()
            elif options==2:
                viewstock()
            elif options==3:
                addtostock()
            elif options==4:
                lessquantprods()
            elif options==5:
                print("------------------------------------------------------------------------------------------------")
                month=input("Enter full name of month of which you want to check sales ")
                if month.title() in month_name:
                    print("Sales of",month,"month are",monthlysales(month))
                else:
                    print("Enter a valid month")
                print("------------------------------------------------------------------------------------------------")
            elif options==6:
                print("------------------------------------------------------------------------------------------------")
                year=int(input("Enter year of which you want to check sales "))
                if len(str(year))==4:   
                    print("Sales of",year,"year are",yearlysales(year))
                else:
                    print("Enter a valid year")
                print("------------------------------------------------------------------------------------------------")
            elif options==7:
                print("------------------------------------------------------------------------------------------------")
                month=input("Enter full name of month of which you want to check purchase ")
                if month.title() in month_name:
                    print("Purchase of",month,"month are",monthlypurchase(month))
                else:
                    print("Enter a valid month")
                print("------------------------------------------------------------------------------------------------")
            elif options==8:
                print("------------------------------------------------------------------------------------------------")
                year=int(input("Enter year of which you want to check purchase "))
                if len(str(year))==4:
                    print("Purchase of",year,"year is",yearlypurchase(year))
                else:
                    print("Enter a valid year")
                print("------------------------------------------------------------------------------------------------")
            elif options==9:
                print("------------------------------------------------------------------------------------------------")
                month=input("Enter full name of month of which you want to check profit ")
                if month.title() in month_name:
                    monthlyprofit(month)
                else:
                    print("Enter a valid month")
                print("------------------------------------------------------------------------------------------------")
            elif options==10:
                print("------------------------------------------------------------------------------------------------")
                year=input("Enter year of which you want to check profit ")
                if len(str(year))==4:
                    yearlyprofit(year)
                else:
                    print("Enter a valid year")
                print("------------------------------------------------------------------------------------------------")
            elif options==11:
                print("Today's Sales are",dailysales())
            elif options==12:
                companyemp()
            elif options==0:
                break
            else:
                print("Enter valid option")
        except ValueError:
            print("Enter a valid option")