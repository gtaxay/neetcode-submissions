class Solution:
    def isPalindrome(self, s: str) -> bool:

        # same back as forward
        # ignore non alphanumeric

        front, back = 0, len(s) - 1
        s = s.lower()

        # if equal add number
        while front < back:
            # skip front if nonalpha
            if not s[front].isalnum():
                front += 1
            elif not s[back].isalnum():
                back -= 1
            else:
                if s[front] != s[back]:
                    return False
                front += 1
                back -= 1
            
        
        return True



        