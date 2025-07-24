n = 3
m = 64
def func(i,n):
    val = 1
    for j in range(1,n+1):
        val = val * i
        
    return val


def NthRoot(n,m):
    for i in range(1, m+1):
        res = func(i, n)
        if res == m:
            return i
        elif res > m:
            break
        
    return -1
        

#print(func(2,3))
print(NthRoot(n,m))


def NthRootO(n,m):
    low = 1
    high = m
    while low<=high:
        mid  = low+ (high-low)//2
        res = func(mid, n)
        if res == m:
            return mid
        elif res > m:
            high  = mid-1
        else:
            low = mid+1
        
    return -1
        

#print(func(2,3))
print(NthRoot(n,m))