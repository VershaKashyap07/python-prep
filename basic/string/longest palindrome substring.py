def longest_palindrome_bruteforce(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                max_length = max(max_length, j - i + 1)
    return max_length,s[:max_length]

#print(longest_palindrome_bruteforce("babad"))


'''TC O(n^3)'''



def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the length of the palindrome
    return right - left - 1

def longestPalindrome(s):
    if not s or len(s) < 1:
        return ""
    
    start, end = 0, 0  # These variables will store the start and end of the longest palindrome
    
    for i in range(len(s)):
        # Check for odd-length palindrome
        len1 = expandAroundCenter(s, i, i)
        # Check for even-length palindrome
        len2 = expandAroundCenter(s, i, i + 1)
        
        # Take the maximum length of the palindrome from the two cases
        max_len = max(len1, len2)
        
        # Update the start and end pointers if a longer palindrome is found
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    # Return the longest palindrome substring
    return s[start:end + 1]

# Test
s = "cbbd"
print(longestPalindrome(s))  # Output: "bb"



def solve(s, i, j):
    if i >= j:
        return True
    if s[i] == s[j]:
        return solve(s, i + 1, j - 1)
    return False

def longest_palindrome(s):
    max_len = 0  # Corrected initial value
    sp = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if solve(s, i, j) == True:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    sp = i

    return s[sp:sp + max_len]  # Corrected slicing

# Test case
s = "babad"
print(longest_palindrome(s))  


