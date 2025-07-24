def removeOuterParentheses(s: str) -> str:
    stack = []
    result = ""
    
    for char in s:
        if char == '(':
            if stack:
                result+=char
            stack.append(char)
        elif char == ')':
            stack.pop()
            if stack:
                result+=char
    
    return result

# Example usage:
s = "(()())(())"
print(removeOuterParentheses(s))  # Output: "()()()"

def removeOuterParentheses(s: str) -> str:
    result = []
    counter = 0
    
    for char in s:
        if char == '(':
            if counter > 0:
                result+=char
            counter += 1
        elif char == ')':
            counter -= 1
            if counter > 0:
                result+=char
    
    return result

# Example usage:
s = "(()())(())"
print(removeOuterParentheses(s))  # Output: "()()()"

