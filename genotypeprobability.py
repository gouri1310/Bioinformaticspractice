k=int(input("Enter the value of k, where k is individuals are homozygous dominant\n"))
n=int(input("Enter the value of n, where n individuals are homozygous recessive\n"))
m=int(input("Enter the value of m, where m individuals are heterozygous\n"))
t=k+m+n
#finding the probability that two randomly selected mating organisms give a dominant phenotype
pk=(k/t)*1#if first individual is homozygous dominant
pn=(n/t)*((k/(t-1))+((m/(t-1))*(1/2)))#if first individual is homozygous recessive
pm=(m/t)*((k/(t-1))+((m-1)/(t-1))*(3/4)+(n/(t-1))*(1/2))#if first individual is heterozygous
prob=pk+pn+pm
print("The probability that two randomly selected mating organisms give a dominant phenotype is {:.5f}".format(prob))
