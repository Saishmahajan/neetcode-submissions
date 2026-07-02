class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapped = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for i in range(len(s)):
            if s[i] in '{[(':
                stack.append(s[i])
            else:    
                if not stack:
                    return False
                a = stack.pop()
                if a != mapped[s[i]]:
                    return False
                
                
        return len(stack) == 0