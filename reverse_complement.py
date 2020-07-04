#reverse complement of a DNA strand is reversing the DNA strand and A&T complement each other and C&G complement each other
fname=input("Enter the file name\n")
f=open(fname)
def reverse(s):
    str=""
    str=s[::-1]
    return(str)
for line in f:
    line=line.rstrip()
    p=reverse(line)
    dna1=p.replace('A','a')
    dna2=dna1.replace('T','t')
    dna3=dna2.replace('G','g')
    dna4=dna3.replace('C','c')
    rev1=dna4.replace('a','T')
    rev2=rev1.replace('t','A')
    rev3=rev2.replace('g','C')
    rev4=rev3.replace('c','G')
print(rev4)
f.close()
