import timeit
start = timeit.default_timer()
#----------------------------------------------------
l=[]
n=1000
'''
for i in range (1,2*n):l+=[int(i*(3*i-1)/2)]
for i in range (n):
    
    I=l[i]
    dif=l[i+1]-l[i]
    for j in range (i,-1,-1):
        
        J=l[j]
        if J<dif:
            break
        test=0
        if (I+J in l):
            #print("+++++",I,J)
            test+=1
        if (abs(I-J) in l):
            #print("-----",I,J)
            test+=1
        if test==2:
            print(I,J,test)
            
        
'''
count=0
for i in range (1,2500):
    for j in range (1,i):
        n=i
        m=j
        
        y1=int((n-m)*((3*(n+m)) -1)/2)
        y2=int((3*(n**2 + m**2)-n-m)/2)

        chk1=((24*y1 +1)**(0.5))%6
        chk2=((24*y2 +1)**(0.5))%6
        c=0
        if chk1==5:
            #print("-----",i,j,y1,y2,chk1,chk2)
            count+=1
            c+=1
        if chk2==5:
            #print("+++++",i,j,y1,y2,chk1,chk2)
            count+=1
            c+=1
        if c==2:
            print(y1,y2,i,j)
            print("answer=",y1)
print("count=",count)









#----------------------------------------------------
end= timeit.default_timer()
print('time=',end-start)
