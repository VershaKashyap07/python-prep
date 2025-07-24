def product_except_self(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [0] * n

    # Compute products of elements to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
        

    # Compute products of elements to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
     

    # Compute the final result
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

# Example usage:
nums = [1, 2, 3, 4]
#print(product_except_self(nums))  # Output: [24, 12, 8, 6]



# Python3 program for A Product Array Puzzle 
def productArray(arr, n): 

	# Base case 
	if n == 1: 
		print(0) 
		return

	temp = 1

	# Allocate memory for the product array 
	prod = [1] *n

	# Initialize the product array as 1 

	# In this loop, temp variable contains product of 
	# elements on left side excluding arr[i] 
    # 'left' will represent the cumulative product of elements to the left of the current element.
	for i in range(n): 
		prod[i] = temp 
		temp *= arr[i] 

	# Initialize temp to 1 for product on right side 
	temp = 1

	# In this loop, temp variable contains product of 
	# elements on right side excluding arr[i] 
    # 'right' will represent the cumulative product of elements to the right of the current element.
	for i in range(n - 1, -1, -1): 
		prod[i] *= temp 
		temp *= arr[i] 

	
	return prod


# Driver Code 
arr = [1,2,3,4] 
n = len(arr) 
print("The product array is: n",productArray(arr, n) ) 


