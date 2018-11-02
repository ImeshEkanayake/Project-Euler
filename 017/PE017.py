a0109=[3,3,4,4,4,3,5,5,4]
a1019=[6,6,8,8,7,7,8,8,8]
a2090=[7,6,6,5,5,7,6,6]
hun=7
AND=3
ten=3

tot=0
for a0 in range (10):
    if a0>0:
        tot+= (a0109[a0-1]+hun)*100
        tot+= AND*99
    for i in a0109: tot+=i
    tot+=ten
    for i in a1019: tot+=i
    for i in a2090: tot+= i*10
    for i in a0109: tot+= i*8
tot+=11
print(tot)
