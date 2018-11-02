def primes_until(x):
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        for j in range (i*2,x+1,i):
            s.discard(j)
    return sorted(s)

n=10000
primes=primes_until(n)
s=set()
d={}
for i in primes:
    I=''.join(sorted(str(i)))
    if I not in s:
        s.add(I)
        d[I]=[i]
    else:
        d[I]+=[i]
for i in sorted(s):
    x=sorted(d[i])
    if len(x)>=3:
        l=len(x)
        
        for j in range (l-2):
            for k in range (j+1,l-1):
                if (x[k]+(x[k]-x[j])) in x:
                    print(str(x[j])+str(x[k])+str(x[k]+(x[k]-x[j])))
            

