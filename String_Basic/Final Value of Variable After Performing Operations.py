operations = ["++X","++X","X++"]
x = 0
for i in operations:
    if i.startswith("--") | i.endswith("--"):
        x-=1
    if i.startswith("++") | i.endswith("++"):
        x+=1
print(x)


from collections import Counter

def finalValueAfterOperations(operations):
    count = Counter(operations)
    print(count)
    return count["++X"] + count["X++"] - count["--X"] - count["X--"]


print(Counter(operations))



x = 0
for ele in operations:
    if ele[1] =='+':
        x+=1
    else:
        x-=1
print(x)























