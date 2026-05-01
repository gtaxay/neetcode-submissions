class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n, m = len(word1), len(word2)
        i = 0
        sol = []

        while i < max(n,m):
            if i < n:
                sol.append(word1[i])
            if i < m:
                sol.append(word2[i])
            
            i += 1
        
        return "".join(sol)

        