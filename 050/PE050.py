def primes_until(x):
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        for j in range (i*2,x+1,i):
            s.discard(j)
    return sorted(s)

n=1000000
primes=primes_until(n)

Max=0
Mc=0
count=0

for i in range (len(primes)):
    tot=primes[i]
    for j in range (i+1,len(primes)):
        tot+=primes[j]
        if tot >n:
                break
        if tot in primes:
            count=j-i+1
            if Mc<count:
                Mc=count
                Max=tot
                print(tot,count,j,i)
    if (j-i+1<Mc):
        break
print("Answer=",Max)
            
            
            
        
        
    
    
    
