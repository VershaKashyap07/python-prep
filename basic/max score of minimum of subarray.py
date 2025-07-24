#max sum of any two consecutive number
arr  = [5, 4, 3, 1, 6] 
n = len(arr)
summ =0
maxi = 0

for k in range(n-1):
    summ =  arr[k]+ arr[k+1]
    maxi = max(maxi, summ)    
            
                    
print(maxi)
         