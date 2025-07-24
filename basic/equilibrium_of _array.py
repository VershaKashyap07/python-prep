from typing import List

def pivotIndex(nums: List[int]) -> int:
	left, pivot, right = 0, 0, sum(nums)-nums[0]
	while pivot < len(nums)-1 and right != left:
		pivot += 1
		right -= nums[pivot]
		left += nums[pivot-1]

	return pivot if left == right else -1

def main():
	# test the function with an example array
	nums = [1, 7, 3, 6, 5, 6]
	result = pivotIndex(nums)
	print(result)

if __name__ == "__main__":
	main()
