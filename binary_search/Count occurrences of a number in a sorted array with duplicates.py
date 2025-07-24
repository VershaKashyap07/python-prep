key = 4
arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = len(arr)

def firstOccurrence(arr,n,key):
    l = 0
    h = n-1
    ans = -1
    while l<=h:
        mid = l+(h-l)//2
        if arr[mid]==key:
            ans = mid
            h = mid-1
        elif arr[mid]<key:
            l = mid+1
        else:
            h = mid-1
    return ans

print(firstOccurrence(arr,n,key))

def lastOccurrence(arr,n,key):
    
    l = 0
    h = n-1
    ans = -1
    
    while l<=h:
        mid = l+(h-l)//2
        if arr[mid]==key:
            ans = mid
            l = mid+1
        elif key<arr[mid]:
            h = mid-1
        else:
            l = mid+1
    return ans

print(lastOccurrence(arr,n,key))

def firstAndLastPosition(arr, n, k):
    first = firstOccurrence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, k)
    return (first, last)

def count(arr, n, x):
    first, last = firstAndLastPosition(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1

print(count(arr, n, key))