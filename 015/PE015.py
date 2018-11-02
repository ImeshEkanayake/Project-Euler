import math
def nCr(n,r):
    t=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return t
k,r=[int(i) for i in input("enter n and r with a space: ").strip().split(" ")]
n=k+r
print(str(n)+"C"+str(r)+" =",int(nCr(n,r)))
