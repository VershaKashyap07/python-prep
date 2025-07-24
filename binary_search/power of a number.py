n = 2
m = 4
def findPower(n,m):
    val = 1
    for i in range(1,n+1):
        val = val * m
        
    return val

print(findPower(n,m))
##optimal
def power(i, p):
    if p == 0:
        return 1  # Base case: i^0 = 1
    elif p % 2 == 0:
        half_power = power(i, p // 2)
        return half_power * half_power  # i^n = (i^(n/2))^2
    else:
        half_power = power(i, (p - 1) // 2)
        return i * half_power * half_power  # i^n = i * (i^((n-1)/2))^2

print(power(2, 2))  # Output will be 1024