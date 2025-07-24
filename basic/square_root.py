# Python3 implementation to find the 
# square root of the number N 
# without using sqrt() function 

# Function to find the square 
# root of the number N using BS 
def sqrtSearch(low, high, N) : 

	# If the range is still valid 
	if (low <= high) :

		# Find the mid-value of the range 
		mid = (low + high) // 2; 

		# Base Case 
		if ((mid * mid <= N) and ((mid + 1) * (mid + 1) > N)) :
			return mid; 

		# Condition to check if the 
		# left search space is useless 
		elif (mid * mid < N) : 
			return sqrtSearch(mid + 1, high, N); 
	
		else :
			return sqrtSearch(low, mid - 1, N); 

	return low; 


N = 25; 
print(sqrtSearch(0, N, N)) 

