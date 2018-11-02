  
import timeit
start = timeit.default_timer()
#----------------------------------------------------
for n in range (134,10000000):
    p=n*(3*n -1)/2
    k=((8*p + 1)**(0.5))/4 +0.25
    
    if(k%1==0):
        print("Answer=",p)
        break













#----------------------------------------------------
end= timeit.default_timer()
print('time=',end-start)
