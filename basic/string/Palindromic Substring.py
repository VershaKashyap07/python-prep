##Brute Force: gen all substrings and then check palindrome
s ="ac"

def count_palindrome(s):
    count =0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check_palindrome(i, j, s):
                count+=1
                
    return count
        
def check_palindrome(i, j, s):
    if i> j:
        return True
    if s[i] ==s[j]:
        return check_palindrome(i+1, j-1, s)
    else:
        return False
        
    
print(count_palindrome(s))   

# optimal: expand around center for odd len string the 
# center should be one char and will check for write and left but in even len the center should be I, i+i 

def countSubstrings(s):
    def expandAroundCenter(s, left, right):
        count = 0
        # Expand while characters on both sides match and we're within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    if not s:
        return 0
        
    total_count = 0
    # Check each position as a potential center
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        total_count += expandAroundCenter(s, i, i)
        # Even length palindromes (between two characters)
        total_count += expandAroundCenter(s, i, i + 1)
    
    return total_count
    
s ='aaa'
print(countSubstrings(s))