class Solution:
    def climbStairs(self, n: int) -> int:

        # repetitive sub problems

        # last two stairs options
        one, two = 1, 1

        # n - 1 because already have 2 variables 
        for _ in range(n - 1):
            temp = one
            one = two + one
            two = temp
        
        # one is the front value
        # similar format to fib
        return one

        