n=1000000
def pu(x):
    if x%2==0:
        x+=1
    s=set()
    for i in range (x,1,-1):
        s.add(i)
        
        for j in range (i*2,x+1,i):
            s.discard(j)
    return sorted(s)
p=pu(n)
q=set()

for i in p:
    tr=1
    I=str(i)
    if len(I)>1:
        while len(I)>0:
            #print(I,end=' ')
            if int(I) in p:
                I=I[1:]
            else:
                tr=0
                break
        if tr>0:
            q.add(i)

            
    I=str(i)
    if len(I)>1:
        while len(I)>0:
            #print(I,end=' ')
            if int(I) in p:
                I=I[:len(I)-1]
            else:
                q.discard(i)
                tr=0
                break
        if tr>0:
            q.add(i)
    
            
print(q)
tot=0

for i in list(q):
    tot+=i
    
print("sum =",tot,'      lenght=',len(q))

