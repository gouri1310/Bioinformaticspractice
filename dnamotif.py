fname=input("Enter the file name\n")
f=open(fname)
c=0
for line in f:
    c+=1
    line=line.rstrip()
    if int(c)==1:
        dna=line
    if int(c)==2:
        dnasub=line
        break
l=int(len(dna))
lsub=int(len(dnasub))
if l>lsub:
    for i in range(l):
        if dna[i:i+lsub]==dnasub:
            print(i+1)

else:
    print(dnasub,"is not a substring of ",dna)
