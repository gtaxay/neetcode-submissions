class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # one from front back

        front, back = 0, len(s) - 1
        s = s.lower()
        while front < back:
            if not s[front].isalnum():
                front += 1
            elif not s[back].isalnum():
                back -= 1
            elif s[front] != s[back]:
                return False
            else:
                front += 1
                back -= 1
        
        return True
        