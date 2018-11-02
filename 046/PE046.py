import timeit
start = timeit.default_timer()
#----------------------------------------------------

def pu(x):
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        for j in range (i*2,x+1,i):
            s.discard(j)
    return sorted(s)
n=10000
primes=pu(n)
sp=[i**2 for i in range(int(n**(0.5))+1)]
for i in range (9,n+1,2):
    chk=0
    
    for j in primes:
        p=(i-j)/2
        if p in sp:
            #print(i,True)
            chk=1
            break
    if chk==0:
        print(i,False)
        break



#----------------------------------------------------
end= timeit.default_timer()
print('time=',end-start)
