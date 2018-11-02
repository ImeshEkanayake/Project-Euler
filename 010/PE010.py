s=set()
p=2000000
for i in range (p,1,-1):
    s.add(i)
    if (i<p/3):
        for j in range (2*i,p+1,i):
            s.discard(j)

y=0
for i in (list(s)):
    y+=i
print(y)
        
    
