n = 28
def floorSqrtB(n):
    ans = 0
    for i in range(1,n+1):
        val = i*i
        if val <= n:
            ans = i
        else:
            break

    return ans


print(floorSqrtB(n))


def floorSqrtO(n):
    low = 1
    high = n
    while low<=high:
        mid = (low+high)//2
        if mid*mid <=n:
            low = mid+1
        else:
            high = mid-1

    return high

print(floorSqrtO(n))