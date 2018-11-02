import timeit
start = timeit.default_timer()    
qwe=set()

for i in range (1,10000):
    n=9-2*len(str(i))+1
    J=10**(int(n+1/2))
    for j in range (1,i+1):
        if j>J:
            break
        k=i*j
        p=str(i)+str(j)+str(k)
        q=set(sorted(p))
        r=0
        if (len(p)==len(q) and k not in qwe and len(q)==9) :
            r=1
            for a in range (1,len(q)+1):
                if str(a) not in q:
                    r=0
                    break
        if r==1:
            qwe.add(k)
            print(len(qwe),")",i,j,k,sorted(q))
            
tot=0
for i in list(qwe):
     tot+=i
print("answer=",tot,len(qwe))

stop = timeit.default_timer()
Time=stop-start
print(Time)
                        
                
                
                
