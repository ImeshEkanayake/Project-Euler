d={}
for i in range (10000+1):
    k=int(i**(0.5))+1
    p=0
    for j in range (1,k):
        if (i%j==0): 
            p+=(i/j) + j
    p-=i
    d[i]=p
q=0
for i in d:
    if (d[i]<=10000):
        if (d[d[i]]==i and i!=d[i]):
            print(i,d[i])
            q+=i

print(q)
