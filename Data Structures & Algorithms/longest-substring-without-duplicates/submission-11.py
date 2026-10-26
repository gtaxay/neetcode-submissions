class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window
        # set bc unique

        window = set()
        length = 0

        left, right = 0, 0
        for c in s:
            # take out duplicates of c
            while c in window:
                window.remove(s[left])
                left += 1
            
            window.add(c)
            length = max(length, len(window))
        
        return length
            


        