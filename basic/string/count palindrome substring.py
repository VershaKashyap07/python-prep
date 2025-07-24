str ="cbbd"

def countSubstrings(str):
    res = 0
    for i in range(len(str)):
        
        # for odd length
        l =i
        r =i
        
        res+= countPalindrome(str,l,r)   
        #for even length
        l = i
        r = i+1
        res+= countPalindrome(str,l,r)
    return(res)
        
def countPalindrome(str,l,r):
    res =0
    while l>=0 and r<len(str) and str[l]==str[r]:
        res+=1
        l-=1
        r+=1
    return res


str ='abba'
print(countSubstrings(str))

#0(n^2)