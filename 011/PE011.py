p=[]
for i in range (20): p=p+[[int(i) for i in input().strip().split(" ")]]
m=0
for i in range (20):
    for j in range (20):
        v,h,dr,dl=0,0,0,0
        if (i<17):
            v=p[i][j]*p[i+1][j]*p[i+2][j]*p[i+3][j]
        if (j<17):
            h=p[i][j]*p[i][j+1]*p[i][j+2]*p[i][j+3]
        if (i<17 and j<17):
            dr=p[i][j]*p[i+1][j+1]*p[i+2][j+2]*p[i+3][j+3]
        if (i<17 and j>2):
            dl=p[i][j]*p[i+1][j-1]*p[i+2][j-2]*p[i+3][j-3]
        q=[v,h,dr,dl]
        if (max(q)>m):
            m=max(q)
        
print("Anster =",m)
