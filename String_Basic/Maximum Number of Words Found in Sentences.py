from typing import List


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
maxvar = 0
count=0
class Solution:
  def mostWordsFound(self, sentences: List[str]) -> int:
    return max(s.count(' ') for s in sentences) + 1


sol = Solution()
print(sol.mostWordsFound(sentences))