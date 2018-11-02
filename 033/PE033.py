l=[]
u=[]
d=[]
for i in range (10,100):
    for j in range (i+1,100):
        k=i/j
        I=sorted(str(i))
        J=sorted(str(j))
        t=0
        com=''
        for a in I:
            if a in J:
                t=1
                com=a
        p=I+J
        p=set(p)
        if t==1 and len(p)==3 and com!='0':
            p.discard(com)
            p=[int(i) for i in p]
            b=max(p)
            a=min(p)
            pk=a/b
            if pk==k and str(a) in str(i):
                print(i,j,"|   |",a,b)
                d+=[b]
                u+=[a]
for i in u:
    if i in d:
        u.remove(i)
        d.remove(i)
print(u,d)
U=1
D=1
for i in u:U*=i
for i in d:D*=i
print("U/D=",U/D,"--------D=",1/(U/D))

