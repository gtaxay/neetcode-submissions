class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        sol = ""

        length = min(len(word1), len(word2))

        for i in range(length):
            sol += word1[i]
            sol += word2[i]

        if length != len(word1):
            sol += word1[length:]
        elif length != len(word2):
            sol += word2[length:]
        
        return sol


        