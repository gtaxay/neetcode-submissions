class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # read backwards and forwards the same
        # sort both and look
        # base case not same length


        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        