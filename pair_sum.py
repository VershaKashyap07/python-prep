def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []
    
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.append([complement, number])
        seen.add(number)
    
    return pairs

# Example usage
numbers = [2, 3, 5, 8, 6, 1]
target = 11
result = find_pairs_with_sum(numbers, target)
print(result)
