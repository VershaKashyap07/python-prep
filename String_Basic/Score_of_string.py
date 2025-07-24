s = 'hello'
score = 0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if j == i+1:
            score += abs(ord(s[i])-ord(s[j]))

print(score)


from itertools import pairwise
summ =0
for a,b in pairwise(map(ord,s)):
    summ += abs(a-b)
print(summ)