class Solution:
    def validPalindrome(self, s: str) -> bool:

        # front and end pointer
        # if different then remove both start and end and check if reverse equals portion 

        left, right = 0, len(s) - 1

        while left < right:

            if s[left] != s[right]:
                skipL, skipR = s[left + 1: right + 1], s[left:right]

                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            
            left += 1
            right -= 1
        
        return True

        