class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        close_to_open = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in close_to_open:
                # Must check if stack exists and the top matches
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        # If stack is empty, all brackets were matched correctly
        return len(stack) == 0