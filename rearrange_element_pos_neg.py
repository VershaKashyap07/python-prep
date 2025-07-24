def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []
  
    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
  
    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]
  
    return A

# Array Initialisation.
A = [1, 2, -4, -5]
ans = rearrange_by_sign(A)
print(ans)

##optimal

def RearrangebySign(A):
    n = len(A)
    
    # Define array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans
    
# Test the function
A = [1,2,-4,-5]
ans = RearrangebySign(A)
print(ans)

# variety when neg!=pos

def variety2(arr):
    neg, pos = [],[]
    for i in range(len(arr)):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    print(pos, neg)

    if len(pos)<len(neg):

        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(pos)*2

        for i in range(len(neg)-len(pos)):
            arr[index]  = neg[len(pos)+i]
            index+=1

    else:
        print("pos is big")
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(neg)*2

        for i in range(len(pos)-len(neg)):
            arr[index]  = pos[len(neg)+i]
            index+=1

    return arr


arr = [1,2,-4,-5,-3,-4]
print(variety2(arr))