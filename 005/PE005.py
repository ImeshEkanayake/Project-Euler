p=int(input("Max multiplyer :"))
num_arr=set();
for i in range (p,1,-1):
    num_arr.add(i)
    if (i<=(p/2)):
        for I in range (2*i,p+1,i):
            num_arr.discard(I)
maxnum=1
print(num_arr)

for i in list(num_arr):
    j=i
    while True:
        if i*j<=p:
            i=i*j
        else:
            break
    print(i)        
    maxnum=maxnum*i
print(maxnum)
