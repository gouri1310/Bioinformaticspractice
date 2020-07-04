n=input("Enter the value of n\n")
n=int(n)
k=input("Enter the value of k\n")
k=int(k)
#The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
#example of the series
#n=5 and k=3, [1,1,4,7,19]
lst=list()
lst.append(1)
lst.append(1)
i=2
while (i<n) and (i>=2):
    p=lst[i-1]+(k*lst[i-2])
    lst.append(p)
    i+=1
print(lst)
print("After ",n,"months the total number according to the series is",lst[n-1])
