
def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    
    return days

def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    maxi = max(weights)
    summation = sum(weights)

    for i in range(maxi, summation + 1):
        if findDays(weights, i) <= d:
            return i

    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)



def leastWeightCapacityO(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacityO(weights, d)
print("The minimum capacity should be:", ans)





