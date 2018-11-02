def pu(x):
    if x%2==0:
        x+=1
    s=set()
    for i in range (x,1,-2):
        s.add(str(i))
        
        for j in range (i*2,x+1,i):
            s.discard(str(j))
    return sorted(s)
p=pu(1000000)
count=0
l=['2','0','4','6','8']
for i in p:
    
    for j in i:
        if j in l:
            break
        
    else:
       
        for a in range (len(i)):
            I=''
            for b in range (a,len(i)):I+=i[b]
            for b in range (a):I+=i[b]
            if I not in p:
                break
        else:
            print('----------',i)
            count+=1
            
            
count+=1# for num 2  
print('count=',count)
    

