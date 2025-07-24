nums = [1,2,3,4,1]
def check(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

print(check(nums))

def optimal(nums):
    hashdec  = {}
    for i in range(len(nums)):
        if nums[i] in hashdec:
            return True
        else:
            hashdec[nums[i]]=1
    return False

print(optimal(nums))



def optimal_2(arr):
    arr.sort()
    for i in range(1,len(arr)):
        
        if arr[i] == arr[i-1]:
            return True
    return False
arr = [1,2,3,4,0]
print(optimal_2(arr))
    


