file=open("a.txt",'r')
f=(file.readlines()[0]).strip().split(',')
alp=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
val={}
k=0
for i in alp:
    k+=1
    val[i]=k

T=set()
k=0
for i in range (1,26):
    k+=i 
    T.add(k)
count=0
for i in f:
    tot=0
    for j in i:
        tot+=val[j]
    if tot in T:
        count+=1
print(count)
