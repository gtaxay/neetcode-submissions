class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        
        window = [0] * 26
        str1 = [0] * 26
 
        # get str1 characters
        for c in s1:
            str1[ord(c) - ord('a')] += 1
        
        # characers in current window
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        # loop through all characters in ewar of s2

        if str1 == window:
            return True
        
        left = 0
        for i in range(len(s1), len(s2)):
            window[ord(s2[left]) - ord('a')] -= 1

            window[ord(s2[i]) - ord('a')] += 1
            left += 1

            if window == str1:
                return True
        
        return False
            
            

        





