# Python3 Implementation of above approach
def minIncrementForUnique(A):
	# sort the array in increasing order
	A.sort()
	
	#counter for no of operations
	ops = 0
	
	# iterate over the array
	for i in range(1, len(A)):
		if A[i] <= A[i-1]:
			ops += A[i-1] - A[i] + 1
			A[i] = A[i-1] + 1
	
	#return no of operations required
	return ops,A

# Driver code
A = [3, 2, 1, 2, 1, 7]
print("Minimum number of increment operations required: ", minIncrementForUnique(A))

# This code is contributed by Jeetu
