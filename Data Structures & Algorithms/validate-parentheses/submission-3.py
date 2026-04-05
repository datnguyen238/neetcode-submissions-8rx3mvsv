class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                n = len(stack)
                if stack:
                    if brackets[char] == stack[n-1]:
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    return False
        return not stack         

        
