#10-05-2023
#R10
#WAP that reads a text file 'lines.txt' and replaces all the occurences of MVN with MVN-43
def REP():
    import os
    F=open("lines.txt",'r+')
    S=F.read()
    print("Original file is:\n"+S)
    print("-------------------------------------------")
    S=S.replace(" MVN "," MVN-43 ")
    F.seek(0)
    os.truncate("lines.txt",0)
    F.write(S)
    print("New file is:\n"+S)

REP()
