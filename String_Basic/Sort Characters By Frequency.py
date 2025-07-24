from collections import Counter, defaultdict
s ="tree"
count = Counter(s)
print(count)
buckets = defaultdict(list)

for char,cnt in count.items():
    buckets[cnt].append(char)
print(buckets)   

res = []
for i in range(len(s) ,0, -1):
    print(i)
    for c in buckets[i]:
        print(c)
        res.append(c*i)
        
print("".join(res))