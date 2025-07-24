# Python3 implementation of the approach

# Function to make array non-decreasing 
def isPossible(a, n) :

	# Take the first element 
	cur = a[0]; 

	# Perform the operation 
	cur -= 1; 

	# Traverse the array 
	for i in range(1, n) : 

		# Next element 
		nxt = a[i]; 

		# If next element is greater than the 
		# current element then decrease 
		# it to increase the possibilities 
		if (nxt > cur) :
			nxt -= 1; 

		# It is not possible to make the 
		# array non-decreasing with 
		# the given operation 
		elif (nxt < cur) :
			return False; 

		# Next element is now the current 
		cur = nxt; 

	# The array can be made non-decreasing 
	# with the given operation 
	return True; 

# Driver code 
if __name__ == "__main__" : 

	a = [ 1,3,1 ]; 
	n = len(a); 

	if (isPossible(a, n)) :
		print("Yes"); 
	else :
		print("No"); 
