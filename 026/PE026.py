q=1000
Max=0
num=0
for i in range (2,q+1):
    p=""
    n=10
    y=1
    t=10**len(str(i))
    while t>0:
        if n>i :
            p+=str(int(n/i))
            n=n%i
            t-=1
        else:
            n=n*10
        if n==0:
            y=0
            break
    t=10**len(str(i))
    if y:
        long=[]
        for I in range (t):
            for J in range (I+1,t):
                s=p[I:J]
                Y=0
                if (J!=len(p)-1):
                    Y=1
                for K in range (t-J):
                
                    if s[K%len(s)]!=p[J+K]:
                        Y=0
                        break
                if Y==1:
                    long+=[int(s)]
                    break
            if Y==1:
                break
        if Max<len(str(min(long))):
            Max=len(str(min(long)))
            num=i
        
print("Answer is",num,"\nLength =",Max)
                               
