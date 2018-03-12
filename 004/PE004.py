# Project Euler 4 --- Largest palindrome product

p=int(input("Enter the number of digits :"))
ul=(10**p) - 1
ll=ul
x=ul
maxnum=0
while ll!=10**(p-1):
    for i in range(x,ll-1,-1):
        k=str(i*ll)
        
        if k==k[::-1] and int(k)>maxnum:
            maxnum=int(k)
            
    ll-=1
print("Maximum palandromin number in rh range is : ",maxnum)
