class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # same characters
        # sort both and look
        # base case not same length

        # map


        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        return sMap == tMap


        