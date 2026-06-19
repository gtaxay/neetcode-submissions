class Solution:
    def isValid(self, s: str) -> bool:

        # matching so stack
        # need hashmap for pop

        cor = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            # how to deal with first case
            # conditions: stack empty and there is some in c return false
            if c in cor:
                if stack and stack[-1] == cor[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True


        