N,M=0,0
for i in range (1,1000000):
    n=i
    c=0
    while (n!=1):
        if (n%2==0):
            n=n/2
        else:
            n=3*n +1
        c+=1
    if c>M:
        N=i
        M=c
        print(i,c)
        
print(N,M)
