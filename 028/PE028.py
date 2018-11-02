while True:
    N=int(input("Enter the num:"))
    n=int(N/2)+1
    l=[1]
    count=0
    p=1
    for i in range (n-1):
        p=p + 8*(i+1)
        l+=[p]
        l+=[p-2*(i+1)]
        l+=[p-4*(i+1)]
        l+=[p-6*(i+1)]
    tot=0
    for i in l:tot+=i
    print("Answer=",tot)
