p=[]
for i in range(100):p+=[int(input())]
print(len(p))
k=0
for i in p:k=k+i
k=str(k)
print(k[0:10],k[-10:-1],k)
