def mergeOverlappingIntervalsB(arr):
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = arr[i][0], arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans


arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
print(mergeOverlappingIntervalsB(arr))

def mergeOverlappingIntervalsO(arr):
    arr.sort()
    ans = []
    for i in range(len(arr)):
        start, end = arr[i][0], arr[i][1]
        if len(ans)!=0 and ans[-1][1]>= start:
            ans[-1][1] =  max(ans[-1][1],end)
        else:
            ans.append([start,end])
            
    return ans
    
print(mergeOverlappingIntervalsO(arr))


