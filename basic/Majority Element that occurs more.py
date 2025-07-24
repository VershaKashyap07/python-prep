def BF_majorityElement(arr):
    # Size of the given array
    n = len(arr)

    for i in range(n):
        # Selected element is arr[i]
        cnt = 0
        for j in range(n):
            # Counting the frequency of arr[i]
            if arr[j] == arr[i]:
                cnt += 1

        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = BF_majorityElement(arr)
print("The majority element is:", ans)


#Time Complexity: O(N2)

#Majority Element that occurs more than N/2 times
arr = [2, 2, 1, 1, 2, 2, 2,1,1]

def OP_majorityElement(arr):
    cnt =0
    ele =0
    cnt1 =0
    for i in range(len(arr)):
        if cnt ==0:
            cnt =1
            ele =arr[i] 
        elif ele ==arr[i]:
            cnt+=1
        else:
            cnt-=1

    # This is only used when we are not sure if n/2  greater ele is there
    #Checking if the stored element is the majority element
    ''''for i in range(len(arr)):
        if arr[i]==ele:
            cnt1+=1
        if cnt1>(len(arr)/2):
        print(ele)
    print(ele)'''

    return ele

ans = OP_majorityElement(arr)
print("The majority element is:", ans)
'''Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.

Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).

Space Complexity: O(1) as we are not using any extra space.'''