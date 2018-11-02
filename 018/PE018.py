n=int(input("Enter the num of raws:"))
p=[]
for i in range(n): p+=[[int(i) for i in input().strip().split(" ")]]

for i in range (n-1,0,-1):
    for j in range (len(p[i-1])):
        if p[i][j]>p[i][j+1]:
            p[i-1][j]+=p[i][j]
        else:
            p[i-1][j]+=p[i][j+1]
print(p[0])
