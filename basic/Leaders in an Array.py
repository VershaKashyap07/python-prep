def printLeaders(arr, n):
    ans = []
  
    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans

n = 6
arr = [10, 22, 12, 3, 0, 6]
print(printLeaders(arr,n))

'''Time Complexity: O(N) 
{ Since the array is traversed single time back to front, it will consume O(N) of time where N = size of the array }.

Space Complexity: O(N) 
{ There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.'''