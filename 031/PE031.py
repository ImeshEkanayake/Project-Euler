p=[1,2,5,10,20,50,100,200]
pn=[int(200/i) for i in p ]
n=200

def chk(val,p,pn,count):
    if val==0:
        count+=1
        return count
    if (len(pn)>0):
        for i in range (pn[0]+1):
            
            if (val-i*p[0])>=0 : 
                count=chk(val-i*p[0],p[1:len(p)],pn[1:len(pn)],count)
            else:
                return count
    return count
print("Answer =",chk(200,p,pn,0))
