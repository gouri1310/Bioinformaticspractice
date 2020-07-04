#the file we are reading has 2 DNA sequences
#hamming distance is the number of corresponding symbols that differ between two strings
#this can be used to get control point mutations in a gene sequence
f=input("Enter the file name\n")
fname=open(f)
l1=list()
l2=list()
seq=list()
hamm=0
for line in fname:
    seq.append(line)
l=len(seq[0])
for i in range(l):
    l1.append(seq[0][i])
    l2.append(seq[1][i])
for j in range(len(l1)):
    if l1[j]!=l2[j]:
        hamm+=1
print(hamm)
