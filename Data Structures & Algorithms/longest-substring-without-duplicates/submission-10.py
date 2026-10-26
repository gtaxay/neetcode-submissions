class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        longest = 0

        while right < len(s):

            while left < right and s[right] in s[left:right]:
                left += 1
            right += 1
        
            

            longest = max(longest, right - left)
        
        return longest
            


                
        