def validPalindrome(str):
    l =0
    r =len(str)-1
    while l<r:
        while l< r and not alphaNum(str[l]):
            l+=1
        while r> l and not alphaNum(str[r]):
            r-=1
        if str[l].lower() != str[r].lower():
            return False
        
        l+=1
        r-=1
    return True

def alphaNum(c):
    return (ord('A')<= ord(c)<=ord('Z') or ord('a')<= ord(c)<=ord('z') or ord('0')<= ord(c)<=ord('9'))

str = "A man, a plan, a canal: Panama"
print(validPalindrome(str))
 