class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        left, right = 0, 0
        longest = 1

        while right < len(s):

            if s[right] not in s[left:right]:
                right += 1
            else:
                while left < right and s[right] in s[left:right]:
                    left += 1
                right += 1
        
            

            longest = max(longest, right - left)
        
        return longest
            


                
        