from random import randrange
import itertools
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def probably_prime(n):
    k=10 #change if you want more accuracy, this is NUMBER OF CHECKS
    
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True



l=itertools.permutations('1234567', 7)
M=0
N=0
for i in l:
    q=int(''.join(i))
    p=probably_prime(int(q))
    if p==True and M<q:
        M=q
print("answer=",M)
