t=0
I=0
while True:
    I+=1
    t+=I
    T=t
    k=0
    for i in range(1,int(T**(0.5))+1):
        if (T%i==0):
            k+=2
    #print(T,k)
    if (k>500):
        break
print(T,k)
