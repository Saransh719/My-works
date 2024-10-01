#09-05-2023
#R5
#WAP that read a text file "Poem.txt" and copies all those words from this file to a new file Temp.txt where the words are of length >4 and starting with 'A' or 'I'(ignore case)

def COPY():
    F=open("Poem.txt",'r')
    nf=open("Temp.txt",'w+')
    S=F.read()
    print("Original file is:\n"+S)
    S=S.split()
    for x in S:
        #print(x.strip().lower())
        if x.strip().lower()[0]in 'a i' and len(x.strip())>4:
            nf.write(x+'\n')
    nf.seek(0)
    S1=nf.read()
    print("\nNew file is:\n"+S1)

COPY()
