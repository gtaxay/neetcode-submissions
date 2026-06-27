class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for c in s:
            
            if c not in pair:
                stack.append(c)
            elif stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                # if its in pair and the prev is not the close
                return False
        
        return len(stack) == 0
        