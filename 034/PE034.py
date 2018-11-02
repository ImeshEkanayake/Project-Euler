import math
fc={}
for i in range (10):fc[str(i)]=math.factorial(i) 
g=0
lim=0
tot=1
print(fc)
while lim<tot:
    tot+=fc['9']
    lim=int(str(lim)+"9")
for i in range (tot):
    k=0
    
    for j in (str(i)):
        k+=fc[j]
        
    
    if i==k:
        print('----------',i)
        g+=i
g=g-fc['1']-fc['2']
print("answer=",g)
