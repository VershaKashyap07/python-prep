command = "G()()()()(al)"

class Solution:
  def interpret(self, command: str) -> str:
    return command.replace('()', 'o').replace('(al)', 'al')
  

sol = Solution()
print(sol.interpret(command))

# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".