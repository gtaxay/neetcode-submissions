class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        left, right = 0, 0
        size = 0

        while right < len(s):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])

            size = max(size, len(window))

            right += 1
        
        return size
        