def bubbleSort(Arr, n):
    swapped = False
    for i in range(n-1,-1, -1):
        for j in range(0, i):
            if Arr[j] > Arr[j+1]:
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
                swapped = True

        if swapped == False:
            break

    return Arr

Arr = [2,71,4,1,5,3]
n = 6
print(bubbleSort(Arr, n))