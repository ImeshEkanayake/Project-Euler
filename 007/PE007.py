P=int(input("Max multiplyer :"))
p=int(P*100/8)
num_arr=set();
for i in range (p,1,-1):
    num_arr.add(i)
    if (i<=(p/2)):
        for I in range (2*i,p+1,i):
            num_arr.discard(I)
num_arr=sorted(num_arr)
print(P,"th prime is ",num_arr[P-1])

