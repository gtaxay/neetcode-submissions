class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {")": "(", "]": "[", "}": "{"}

        stack = []
        for c in s:
            if c not in valid:
                stack.append(c)
            elif not stack or stack.pop() != valid[c]:
                return False

        if stack:
            return False
            
        return True

                

        