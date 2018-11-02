P=[i**5 for i in range (10)]
print(P)
n=0
for i in range (2,1000000):
    k=0
    for j in str(i):
       k+=P[int(j)]
    if k==i:
        print(i,k)
        n+=k
print("Answer=",n)
