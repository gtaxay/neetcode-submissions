class Solution:
    def isPalindrome(self, s: str) -> bool:

        front, back = 0, len(s) - 1
        s = s.lower()

        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while back > front and not s[back].isalnum():
                back -= 1
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
        
        return True
            
        