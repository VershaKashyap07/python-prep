s = "abc"
t = "bac"

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {c: i for i, c in enumerate(s)}
        total_diff = 0
        for i, c in enumerate(t):
            total_diff += abs(d[c] - i)
        return total_diff

sol = Solution()
print(sol.findPermutationDifference(s, t))
