import math
d=[]
Pos={}
n=1000000
q=[]
v=10
for i in range (v):
    d+=[math.factorial(i)]
    Pos[i]=0
    q+=[i]
p=len(d)-1

while n>0:
    if d[p]>=n:
        p-=1
    if p<0:
        break
    n-=d[p]
    Pos[p]+=1


num=""
for i in range (9,0,-1):
    num=num+str(q[Pos[i]])
    q.pop(Pos[i])
num+=str(q[0])
print(num)
