import math

def smallestDivisor(arr, limit):
    n = len(arr)  # size of array
    maxi = max(arr)
    # Find the smallest divisor
    for d in range(1, maxi+1):
        # Find the summation result
        sum = 0
        for i in range(n):
            sum += math.ceil(arr[i] / d)
        if sum <= limit:
            return d
    return -1

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)


def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisorO(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisorO(arr, limit)
print("The minimum divisor is:", ans)





