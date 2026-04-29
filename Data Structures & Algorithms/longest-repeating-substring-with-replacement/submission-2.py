class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0,0

        longest = 0

        total = {}

        while right < len(s):

            total[s[right]] = 1 + total.get(s[right], 0)

            print(total)

            while max(total.values()) <= (right - left - k):
                total[s[left]] -= 1
                left += 1
            
            right += 1

            longest = max(longest, right - left)
                

        
        return longest
        