def primes_until(x):
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        for j in range (i*2,x+1,i):
            s.discard(j)
    return s


primes=primes_until(1500000)

#=====================================

p1000=sorted(primes_until(1000))
sqr=[i**2 for i in range (1000)]
p1000.reverse()
I,J=0,0
MAX=0
for i in  (p1000):
    for j in (p1000):
        
        count=0
        for k in range (1000):
            n=sqr[k]+j*k+i
            if n in primes:
                count+=1
            else:
                break
        if count>MAX:
            MAX=count
            I=i
            J=j
            print(j,i,count)

            
        count=0
        for k in range (1000):
            n=sqr[k]-j*k+i
            if n in primes:
                count+=1
            else:
                break
        if count>MAX:
            MAX=count
            I=i
            J=-j
            print(J,I,count)
        
print("answer=",I*J)
                
    

