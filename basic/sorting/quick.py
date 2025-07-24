def quicksort(Arr, low, high):
    if low < high:
        pi = partition(Arr, low, high)
        quicksort(Arr, low, pi - 1)  # left subarray
        quicksort(Arr, pi + 1, high)  # right subarray


def partition(Arr, low, high):
    pivot = Arr[low]
    i = low
    j = high

    while i < j:
        ##Arr[i] <= pivot to decide where we want to keep element same as pivot in this case , it's on left
        while i < high and Arr[i] <= pivot:
            i += 1
        while j > low and Arr[j] > pivot:
            j -= 1
        if i < j:
            Arr[i], Arr[j] = Arr[j], Arr[i]

    # when j crossed i change pivot and put at it's correct place
    Arr[low], Arr[j] = Arr[j], Arr[low]
    return j  # partition index pi


Arr = [13, 5, 4, 200, 10, 0]

quicksort(Arr,0,len(Arr)-1)
print(Arr)
