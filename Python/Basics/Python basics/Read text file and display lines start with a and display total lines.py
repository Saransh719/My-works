#09-05-2023
#WAP to read a text file 'lines.txt' and display all the lines that start with the alphabet A and also display the count of lines

def READF():
    F=open('lines.txt','r')
    L=F.readlines()
    print("The file is:")
    for line in L:
        line=line.strip()
        print(line)



def FUN():
    print("\nLines starting with letter A are:")
    c=0
    F=open('lines.txt','r')
    L=F.readlines()
    for line in L:
        line=line.strip()
        if line[0]=='A':
            print(line)
            c+=1
    print("\ncount=",c)

READF()
FUN()

