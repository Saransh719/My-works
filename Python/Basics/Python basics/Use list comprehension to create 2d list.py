#02-05-2023
#R6(b)
'''Using list comprehension create a 2d list for storing marks in 5 subjects for n students'''
def CLIST(n):
    L=[[(int(input("enter marks in {} subject for {} student ".format(j+1,i+1)))) for j in range(5)] for i in range(n)]
    print("Your list of marks is",L)

n=int(input("Enter no of students "))
CLIST(n)
