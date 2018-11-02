import itertools
import timeit
start = timeit.default_timer()

l=itertools.permutations('0123456789', 10)
tot=0

for i in l:
    p=1
    if (i[0]=='0' or int(i[3])%2!=0 or (int(i[2])+int(i[3])+int(i[4]))%3!=0 or i[5]!='5'):
        p=0
        continue
    if int(i[4]+i[5]+i[6])%7!=0:
        p=0
        continue
    if int(i[5]+i[6]+i[7])%11!=0:
        p=0
        continue
    if int(i[6]+i[7]+i[8])%13!=0:
        p=0
        continue
    if int(i[7]+i[8]+i[9])%17!=0:
        p=0
        continue
    if p==1:
        tot+=int(''.join(i))
print("answer=",tot)
end = timeit.default_timer()
print("time=",end-start)
