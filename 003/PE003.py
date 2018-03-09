print("Project Euler 3 - Largerst Prime Factor")
P=int(input("Ehter the number :"))
limit=int(P*(0.5))+1
S=1
for i in range (2,limit):
    #print(P%i,i)
    while P%i==0:
        P=P/i
        S=i
    if i>P:
        break
if S==1:
    S=P

print("The largest prime is ",S)
        
        
        
