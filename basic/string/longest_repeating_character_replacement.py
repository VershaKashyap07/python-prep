# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Brute: gen all substring and then find the no of conversions (min)

s = "AABABBA"
k =1
max_length = 0
n = len(s)

for i in range(n):
    for j in range(i, n):
        substring = s[i:j+1]
    
        char_count = {}
        for c in substring:
            char_count[c] = char_count.get(c,0)+1
           
        max_freq =  max(char_count.values())
        if len(substring) - max_freq <=k:
            max_length = max(max_length,len(substring))
            
            
print(max_length) 
            
# Time Complexity: O(n³) where n is the length of the string:

# O(n²) to generate all substrings
# O(n) to count characters in each substring

# Space Complexity: O(1) since we only store character frequencies (maximum 26 characters)      

##Better
def opt_longest_repeating_character_replacement(s, k):
    l=0
    count ={}
    res =0
    maxf =0

    for r in range(len(s)):
        count[s[r]] =  count.get(s[r],0)+1
        maxf = max(maxf,count[s[r]])
            
        while (r-l+1) -maxf > k:
            count[s[l]]-=1
            l+=1

        res  = max(res, r-l+1)

    return res

# Test the function
s = "ABAB"
k = 2
print("opt_longest_repeating_character_replacement",opt_longest_repeating_character_replacement(s, k))  # Output: 4

#Optimal


def characterReplacement(s: str, k: int) -> int:
    if not s:
        return 0
        
    # Initialize character frequency map and variables
    char_count = {}
    max_length = 0
    max_count = 0  # Count of most frequent character in current window
    left = 0       # Left pointer of sliding window
    
    # Iterate through string using right pointer
    for right in range(len(s)):
        # Update frequency of current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update max_count if current character becomes most frequent
        max_count = max(max_count, char_count[s[right]])
        
        # Current window size
        window_size = right - left + 1
        
        # If number of characters to replace exceeds k, shrink window
        if window_size - max_count > k:
            # Decrease frequency of character going out of window
            char_count[s[left]] -= 1
            left += 1
        else:
            # Update max_length if current window is valid
            max_length = max(max_length, window_size)
    
    return max_length

print(characterReplacement(s, k))


