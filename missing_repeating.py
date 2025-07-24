arr =[3,1,2,5,4,6,7,5]
n = len(arr)

def findMissingRepeatingNumbersBrute(arr,n):
    repeat, missing = -1,-1
    for i in range(1,n+1):
        cnt =0
        for j in range(n):
            if arr[j]== i:
                cnt+=1
        if cnt==2:
            repeat = arr[j]
            
        elif cnt ==0:
            missing = i
        if repeat!=-1 and missing!=-1:
            break
    return repeat, missing
    
print(findMissingRepeatingNumbersBrute(arr,n))


def findMissingRepeatingNumbersBetter(arr,n):
    hash = [0]*(n+1)
    repeating, missing = -1,-1

    for i in range(n):
        hash[arr[i]]+=1

    for i in range(1, n+1):
        if hash[i] ==2:
            repeating = i

        elif hash[i]== 0:
            missing = i

        if repeating !=-1 and missing !=-1:
            break

    return [repeating, missing]

print(findMissingRepeatingNumbersBetter(arr,n))


def findMissingRepeatingNumbersOptimal1(a):
    n = len(a)  # size of the array

    # Find Sn and S2n:
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    # Calculate S and S2:
    S, S2 = 0, 0
    for i in range(n):
        S += a[i]
        S2 += a[i] * a[i]

    # S-Sn = X-Y:
    val1 = S - SN

    # S2-S2n = X^2-Y^2:
    val2 = S2 - S2N

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]


 
print(findMissingRepeatingNumbersOptimal1(arr))


def findMissingRepeatingNumbersOptimal2(a):
    n = len(a) # size of the array

    xr = 0

    #Step 1: Find XOR of all elements:
    for i in range(n):
        xr = xr ^ a[i]
        xr = xr ^ (i + 1)

    #Step 2: Find the differentiating bit number:
    number = (xr & ~(xr - 1))

    #Step 3: Group the numbers:
    zero = 0
    one = 0
    for i in range(n):
        #part of 1 group:
        if ((a[i] & number) != 0):
            one = one ^ a[i]
        #part of 0 group:
        else:
            zero = zero ^ a[i]

    for i in range(1, n + 1):
        #part of 1 group:
        if ((i & number) != 0):
            one = one ^ i
        #part of 0 group:
        else:
            zero = zero ^ i

    # Last step: Identify the numbers:
    cnt = 0
    for i in range(n):
        if (a[i] == zero):
            cnt += 1

    if (cnt == 2):
        return [zero, one]
    return [one, zero]

if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbersOptimal2(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n") 





