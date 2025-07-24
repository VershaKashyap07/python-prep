key = 8
arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = len(arr)

def findfirst(arr,n,key):
    ##lower bound
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

print(findfirst(arr,n,key))

def findlast(arr,n,key):
    ##lower bound
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

print(findlast(arr,n,key))