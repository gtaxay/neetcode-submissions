class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(openB, closeB, current):

            #stop case

            if closeB > openB or (openB + closeB) > n * 2:
                return 

            # base case

            if closeB == openB == n:
                res.append("".join(current))
                return
            
            # DFS
            if openB < n:
                current.append("(")
                backtrack(openB + 1, closeB, current)
                current.pop()
            
            if closeB < openB:
                current.append(")")
                backtrack(openB, closeB + 1, current)
                current.pop()

            

        

        backtrack(0, 0, [])
        return res
        