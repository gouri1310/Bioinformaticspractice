#A DNA strand is transcribed to an RNA strand by replacing T(thymine) by U(Uracil)
f=input("Enter the file name\n")
fname=open(f)
for line in fname:
    line=line.rstrip()
    rna=line.replace("T","U")
print(rna,"\n")
fname.close()
