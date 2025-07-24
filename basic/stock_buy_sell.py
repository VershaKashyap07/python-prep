#brute force method
arr = [7, 1, 5, 3, 6, 9]
maxpro = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j]> arr[i]:
            maxpro = max(arr[j]-arr[i],maxpro)
print(maxpro)
        

def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        #print("min",minPrice)
        maxPro = max(maxPro, arr[i] - minPrice)
        #print("max",maxPro)
    return maxPro


maxPro = maxProfit(arr)
print("Max profit is:", maxPro)

'''Time complexity: O(n)

Space Complexity: O(1)'''