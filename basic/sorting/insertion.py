def insertionSort(Arr,n):
    for i in range(n):
        j =i
        while(j>0 and Arr[j-1]> Arr[j]):
            Arr[j-1], Arr[j] = Arr[j], Arr[j-1]
            j-=1
        

    return Arr

Arr = [2,7,4,11,5,3]
n = 6
print(insertionSort(Arr, n))