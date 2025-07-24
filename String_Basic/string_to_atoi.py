s = "1337c0d"
res = 0
sign = 1
def atoi(s,res,sign):
    s.strip()
    
    if len(s) ==0:
        return 0
        
    if s[0] =='-' or s[0] =='+':
        if s[0] =='-':
            sign =-1
        s = s[1:]
    
    for char in s:
        if not char.isdigit():
            break
        res = res*10 + int(char)
        
    if res < -2**31:
        return -2**31
    if res > 2**31 -1:
        return 2**31 -1
        
    return res
print(atoi(s,res,sign))
        

    
        