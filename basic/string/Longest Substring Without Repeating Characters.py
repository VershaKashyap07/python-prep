def solve(s: str) -> int: 
    if len(s) == 0:
        return 0
    maxans = 0
    for i in range(len(s)):
        seen = {}
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen[s[j]] = 1
            maxans = max(maxans, j - i + 1)
    return maxans

s = 'aabc'    
print(solve(s))  # Output: 3

##Better
def solve(str: str) -> int:
    if len(str) == 0:
        return 0
    maxans = float("-inf")
    setx = set()
    l = 0
    for r in range(len(str)):  # outer loop for traversing the string
        if str[r] in setx:  # if duplicate element is found
            while l < r and str[r] in setx:
                setx.remove(str[l])
                l += 1
        setx.add(str[r])
        maxans = max(maxans, r - l + 1)
    return maxans

##optimal
def lengthofLongestSubstring(s: str):
        mpp = [-1] * 256
        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)

            mpp[ord(s[right])] = right

            length = max(length, right - left + 1)
            right += 1
        return length

s = 'aabc'    
print(lengthofLongestSubstring(s))


    



    

    
