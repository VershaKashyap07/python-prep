arr = [9, -3, 3, -1, 6, -5]
n = len(arr)
maxcnt = 0
for i in range(n):
    for j in range(i,n):
        summ ,cnt =0,0
        for k in range(i, j+1):
            summ+= arr[k]
            
        if summ ==0:
            maxcnt = max(j-i+1, maxcnt)
                
print(maxcnt)
                

arr = [9, -3, 3, -1, 6, -5]
n = len(arr)

def maxlen(arr,n):
    maxcnt = 0
    hashmap = {}
    summ =0
    for i in range(n):
        summ += arr[i]
        if summ ==0:
            maxcnt = i + 1
        else:
            if summ in hashmap:
                maxcnt =  max(maxcnt, i- hashmap[summ])
            else:
                hashmap[summ] = i
    return maxcnt
    
print(maxlen(arr,n))