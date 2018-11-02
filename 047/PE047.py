import timeit
start = timeit.default_timer()
#----------------------------------------------------

n=10000000
def pu(x):
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        for j in range (i*2,x+1,i):
            s.discard(j)
    return sorted(s)
primes=pu(n)
c=[]
count=0
for i in range (1,n):
    I=i
    q=set()
    
    for j in primes:
        #print(i,I,j)
        
        while I%j==0:
            I=I/j
            q.add(j)
            if I==1:
                break
        if I==1:
            break
        
    if I>1:
        q.add(I)
    c+=[len(q)]
    if len(q)==4:
        count+=1
    else:
        count=0
    
    if count==4:
        k=len(c)
        print(k,k-1,k-2,k-3)
        print("Answer=",k-3)
        break
    









#----------------------------------------------------
end= timeit.default_timer()
print('time=',end-start)
