#13-04-2023
#R1
'''
Write a menu driven program to call the following functions as per user's choice
a)Decimal to Binary
b)Binary to Decimal
c)Decimal to Octal
d)Octal to Decimal
e)Decimal to Hex
f)Hex to Decimal
'''
def D2B(a):
    s=""
    while a:
        s=s+str(a%2)
        a=a//2
    s=s[::-1]
    return(s)
def B2D(a):
    s=0
    a=str(a)
    i=len(a)-1
    for x in a:
        x=int(x)
        s+=x*(2**i)
        i-=1
    return(s)

def D2OCT(a):
    s=""
    while a:
        s=s+str(a%8)
        a=a//8
    s=s[::-1]
    return(s)

def OCT2D(a):
    s=0
    a=str(a)
    i=len(a)-1
    for x in a:
        x=int(x)
        s+=x*(8**i)
        i-=1
    return(s)

def D2HEX(a):
    d={'10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}
    s=""
    while a:
         rem=str(a%16)
         if rem in d:
             s+=d[rem]
             a=a//16
         else:
             s+=rem
             a=a//16
    s=s[::-1]
    return(s)

def HEX2D(a):
    d={'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15'}
    s=0
    a=str(a)
    i=len(a)-1
    for x in a:
        if x in d:
           x=d[a]
        x=int(x)
        s+=x*(16**i)
        i-=1
    return(s)
#__main__
while True:
    ans=input('''
1 for Decimal to Binary
2 for Binary to Decimal
3 for Decimal to Octal
4 for Octal to Decimal
5 for Decimal to Hex
6 for Hex to Decimal
0 for exit
''')
    num=int(input("enter number "))
    if ans=='1':
        print("binary is", D2B(num))
    elif ans=='2':
        print("decimal is", B2D(num))
    elif ans=='3':
        print("octal is", D2OCT(num))
    elif ans=='4':
        print("decimal is", OCT2D(num))
    elif ans=='5':
        print("Hex is", D2HEX(num))
    elif ans=='6':
        print("decimal is", HEX2D(num))
    elif ans=='0':
        break
    else:
        print("Enter a valid options")
