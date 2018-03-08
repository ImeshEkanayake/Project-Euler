print("Project Euler 002 ")
P=int(input("Enter the range :"))

a,b=1,1
Sum=0
while (a<P and b<P):
    a,b=b,a+b
    if str(b)[-1] in ['2','4','6','8','0'] and b<P: #Division cost more time
        Sum+=b
        
print("The and sum of the Even numbers =",Sum)
