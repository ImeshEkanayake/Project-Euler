D=[9,90*2,900*3,9000*4,90000*5,900000*6,]
tot=1
for i in range (7):
    d=10**i
    j=0
    while (d-D[j]>0):
        d=d-D[j]
        j+=1
    m=d%(j+1)
    n=d//(j+1)
    #print(10**i,d,n,m)
    p=int(str(10**(i-1) + n)[m-1])
    tot*=p
print('answer=',tot)
