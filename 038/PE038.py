p=[]
for i in range (1,10000):
    a=''
    t=1
    
    while len(a)<9:
        a+=(str(i*t))
        t+=1
        if t>10:
            break
    if (len(a)==9 and len(set(a))==9 ):
        if '0' not in a:
            p+=[int(a)]
print(sorted(p))
print('Answer=',max(p))
            
