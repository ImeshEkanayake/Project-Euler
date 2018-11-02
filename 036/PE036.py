n=1000000
def pal(x):
    x=str(x)
    for i in range (int(len(x)/2)+1):
        if x[i]!=x[-(i+1)]:
            break
    else:
        return 1
    return 0
tot=0
for i in range (n):
    I=bin(i)[2:]
    if (pal(i) and pal(I)):
        tot+=i
        print(i)
print("total=",tot)
    
