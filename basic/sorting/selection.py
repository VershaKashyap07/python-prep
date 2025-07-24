def selectionSort(Arr,n):
    for i in range(n):
        min_value  = i
        
        for j in range(i+1,n):
            if Arr[j] < Arr[min_value]:
                min_value = j

        Arr[i], Arr[min_value]  = Arr[min_value], Arr[i]
    
    return Arr


Arr = [2,7,4,1,5,3]
n = 6
print(selectionSort(Arr, n))

