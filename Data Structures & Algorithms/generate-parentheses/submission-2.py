class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can only add open if less than n
        # can only add closed if less than open
        # base case return if open == closed == n

        res = []

        def backtrack(openB, closeB, current):
            if openB == closeB == n:
                res.append("".join(current))
            
            if openB < n:
                current.append("(")
                backtrack(openB + 1, closeB, current)
                current.pop()
            
            if closeB < openB:
                current.append(")")
                backtrack(openB, closeB + 1, current)
                current.pop()
        
        backtrack(0,0,[])
        return res
        