class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # funciton to check is Palidrone
        # stop case index is out of bounds
        # need a path var

        res = []
        path = []

        def backtrack(index):
            if index >= len(s):
                res.append(path.copy())
                return 
            
            # how do you know the substrings
            for j in range(index, len(s)):
                if self.isPali(index, j, s):
                    path.append(s[index:j+1])
                    backtrack(j+1)
                    path.pop()

        
        # start at first character
        backtrack(0)
        return res

    def isPali(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True



        