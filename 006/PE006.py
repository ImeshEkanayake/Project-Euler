p=int(input("sum of the sqr and sqr of the cum different of first ="))
Ss=0
sS=0
for i in range (1,p+1):
    Ss+=i**2
    sS+=i
print("answer = ",(sS**2)-Ss)
