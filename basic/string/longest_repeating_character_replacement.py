def longest_repeating_character_replacement(s, k):
    max_length = 0

    # Try all possible replacements within the given limit k
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            max_count = max(substring.count(char) for char in set(substring))

            # Check if it's possible to make the substring repeating by replacing characters
            if len(substring) - max_count <= k:
                max_length = max(max_length, len(substring))

    return max_length

# Test the function
s = "ABAB"
k = 2
print(longest_repeating_character_replacement(s, k))  # Output: 4



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



