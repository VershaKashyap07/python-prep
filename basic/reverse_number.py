def stringPalindrome(str,pos):
    if pos > len(str)/2:
        return True
    if str[pos]!= str[len(str)-pos-1]: #base cond
        return False
    return stringPalindrome(str, pos+1)

print(stringPalindrome("mam",0))