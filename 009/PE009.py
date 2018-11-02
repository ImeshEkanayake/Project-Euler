for i in range (1000):
    for j in range (i,1000-i):
        k=1000-i-j
        if k>j:
            if (i**2+j**2==k**2):
                print (i,j,k)
                I,J,K=i,j,k
print("abc =",I*J*K)
                
