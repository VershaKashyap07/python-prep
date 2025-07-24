arr = [1,2,2,3,2]
n = len(arr)
res =0
ls =[]
def majorityBrute(n,arr):
    for i in range(n):
        if len(ls) ==0 or ls[0]!= arr[i]:
            count =0
            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1
                
            res = n//3
            if count>res:
                ls.append(arr[i])
            
        if len(ls) == 2:
            break
        
    return ls 
print(majorityBrute(n,arr))

res =[]
ls = {}
def majorityBetter(n,arr):
    # we can use counter here instead of loop
    # counter  = Counter(arr)
    for i in arr:
        a =  ls.get(i, 0)+1
        ls[i] = a
        
    for k,v in ls.items():
        if v>n//3:
            res.append(k)
            
    return res 
print(majorityBetter(n,arr))

def majorityoptimal(n,arr):
    cnt1, cnt2, ele1, ele2 = 0,0,0,0
    ls = []
    for i in range(n):
        if cnt1==0 and ele2!=arr[i]:
            cnt1+=1
            ele1 = arr[i]
            
        elif cnt2==0 and ele1!=arr[i]:
            cnt2+=1
            ele2 = arr[i]
            
        elif arr[i] == ele1:
            cnt1+=1
        
        elif arr[i] == ele2:
            cnt2+=1
        
        else:
            cnt1-=1
            cnt2-=1
            
      
    
    cnt1, cnt2 = 0,0
    for i in range(n):
        if arr[i] == ele1:
            cnt1+=1
        elif arr[i] ==ele2:
            cnt2+=1
    
    if cnt1>n//3:
        ls.append(ele1)
    if cnt2>n//3:
        ls.append(ele2)
        
    return ls
        
print(majorityoptimal(n,arr))