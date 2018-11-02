M,P=0,""
for i in range (20):P=P+input()
for i in range (1000-13):
    k=1
    for i in range (i,i+13):k=k*int(P[i])
    if M<k:M=k
print(M)
