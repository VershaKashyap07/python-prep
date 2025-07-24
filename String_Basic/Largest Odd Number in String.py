def largest_odd_substring(num):
    for i in range(len(num)-1, -1,-1):
        if int(num[i])%2!=0:
            return num[:i+1]
    return ""
num = "35287"
print(largest_odd_substring(num))

# find largest odd digit
s = "4206"
num = int(s)

def check(num):
    maxi = float('-inf')
    num1 = num
    if num%2==0:
        while num>0:
            digit = num%10
            if digit%2!=0:
                if digit > maxi:
                    maxi = digit
                    
            num//=10
        if maxi == float('-inf'):
            return num1
        else:
            return maxi
    else:   
        return num

print(check(num))
    
    
    

    
    

