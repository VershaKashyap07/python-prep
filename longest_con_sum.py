arr = [102,4,100,1,101,3,2,1,1]
n =len(arr)

def longestSuccessiveElements(arr):
    x, cnt,longest = 0,0,0
    for i in range(n):
        x = arr[i]
        cnt =1
        
        while ls(arr,x+1):
            x =x+1
            cnt+=1
        longest = max(longest, cnt)
        
    return longest
    
def ls(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
       
    return False
    
print(longestSuccessiveElements(arr))

#better approach
last_smaller = float('-inf')
mini = 0
cnt=1
longest = 0
arr.sort()
print(arr)

for i in range(n):
    mini = arr[i]-1
    if last_smaller == mini:
        cnt+=1
        last_smaller = arr[i]
        
    elif last_smaller != arr[i]:
        cnt=1
        last_smaller = arr[i]
        
    longest = max(longest,cnt)
print(longest)      

#optimal
st =set()

cnt=1
longest = 0

for i in range(n):
    st.add(arr[i])
print(st)   

for j in st:
    if j-1 not in st:
        cnt = 1
        x = j
        
        while x+1 in st:
            x+=1
            cnt+=1
            
        longest = max(longest,cnt)
        
print(longest)