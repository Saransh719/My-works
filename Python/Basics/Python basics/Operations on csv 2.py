#08-08-2023
#R16
'''Considering the file emp.csv, create a menu driven program to do the following operations
a)Show Department wise records
b)Total salary paid to specific department'''

import csv
def Deprec():
    dept=[]
    with open("emp.csv",'r') as F:
        Rob=csv.reader(F)
        for deptsearch in Rob:
            if deptsearch[3] not in dept:
                dept.append(deptsearch[3])
        F.seek(0)
        for x in dept:
            print("Records of",x,"department are")
            for y in Rob:
                if y[3]==x:
                    print(y)
            F.seek(0)

def depsal():
    dept=[]
    sum=0
    with open("emp.csv",'r') as F:
        Rob=csv.reader(F)
        for deptsearch in Rob:
            if deptsearch[3] not in dept:
                dept.append(deptsearch[3])
        F.seek(0)
        for x in dept:
            print("Sum of",x,"department is")
            for y in Rob:
                if y[3]==x:
                    sum+=int(y[2])
            print(sum)
            sum=0
            F.seek(0)
#__main__
Deprec()
depsal()
