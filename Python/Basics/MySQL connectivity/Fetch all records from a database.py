#22-09-2023
#C1
#WAP that fetches all the records from employee table which is in alpha database
import pymysql as p
con1=p.connect(host='localhost',user='root',passwd='',database="alpha")
cur1=con1.cursor()
cur1.execute("select * from employee")
print("ID Name Salary Desig")
for rec in cur1.fetchall():
        print(rec[0],str(rec[1])+" ",rec[2],rec[3])
