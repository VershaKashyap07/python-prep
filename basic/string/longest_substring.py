def solve(str):
    if len(str) == 0:
        return 0
    maxans = -1
    for i in range(len(str)):  # outer loop for traversing the string
        set = {}
        # nested loop for getting different string starting with str[i]
        for j in range(i, len(str)):
            if str[j] in set:  # if element if found so mark it as ans and break from the loop
                maxans = max(maxans, j - i)
                break
            set[str[j]] = 1
    return maxans


str = "takeUforward"
#print("The length of the longest substring without repeating characters is", solve(str))


##########optimal ####################

def lengthofLongestSubstring(str):
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

str = "takeUforward"
    
#print("The length of the longest substring without repeating characters is",lengthofLongestSubstring(str))



def lengthofLongestSubstring(s):
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


if __name__ == "__main__":
    str = "takeUforward"
    print("The length of the longest substring without repeating characters is",
          lengthofLongestSubstring(str))
    
