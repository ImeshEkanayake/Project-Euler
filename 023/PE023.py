n=int(input("enter the num (until):"))
D=[]
d=[]
tot=0
for i in range (1,n+1):
    k=int(i**(0.5))+1
    p=0
    for j in range (1,k):
        qwe=i/j
        if (qwe==int(qwe)):
            p+=(j+qwe)
        if (j==qwe):
            p-=j
    p-=i
    if p>i:
        d+=[i]
    q=0
    for m in range (len(d)-1,-1,-1):
       if ((i-d[m]) in d):
            q=1
            break
    if (q==0):
        D+=[i]
        tot+=i
        print(i)
k=0
print(tot,len(D))
    
        
        
