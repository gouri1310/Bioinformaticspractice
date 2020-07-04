#code to get the GC content of a DNA sequence
fname=input("Enter the file name\n")
f=open(fname)
def gc_content(s):
    l=len(s)
    c=s.count('C')
    g=s.count('G')
    p=((c+g)/l)*100
    return p
dna=dict()
for line in f:
    line=line.rstrip()
    if line.startswith('>'):
        words=line.split()
        name=words[0][1:]
        dna[name]=""
    else:
        dna[name]=dna[name]+line
ls=list()
for v in dna.values():
    ls.append(gc_content(str(v)))
maxi=max(ls)
for k,v in dna.items():
    temp=gc_content(str(v))
    if temp==float(maxi):
        print(k,"\n")
        print("{:.3f}".format(maxi))
        break
f.close()
