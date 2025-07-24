s = "()(())((()()))"
res, curr =0,0
for i in s:
    if i=='(':
        curr+=1
    elif i==')':
        curr-=1
    res = max(res, curr)

print(res)