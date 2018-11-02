a=sorted('QWERTYUIOPLKJHGFDSAZXCVBNM')
b={}
n=1
for i in a:
   b[i]=n
   n+=1
print(b)
f=open("f.txt",'r')
data=(f.readlines())
print(len(data))
data=sorted(data[0].strip().split(','))
print(len(data))
tot=0
n=0

for i in data:
    k=0
    n+=1
    for j in i: 
        if j!='"':
           k+=b[j]
    val= n*k
    tot=tot+val
print(tot)
