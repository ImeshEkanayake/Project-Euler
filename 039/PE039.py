Max=0
Num=0
for p in range (3,1000):
    count=0
    for i in range (int(p/2)-1,int(p/3),-1):
        for j in range (i,int(i/2)-1,-1):
            k=p-i-j
            if (i**2==j**2+k**2):
                
                count+=1
    if count>Max:
        Max=count
        Num=p
        print(p,count)
print("Max count P =",Num)
