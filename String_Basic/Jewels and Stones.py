jewels = "z"
stones = "ZZ"
s = set(jewels)
count = 0
for i in stones:
    if i in s:
        count+=1
print(count)



class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int: 
        count = 0
        mpp ={}
        for i in stones:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i]=1
    
        for j in jewels:
            if j in mpp:
                count += mpp[j]
            else:
                count+=0

        return count
        