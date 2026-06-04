class Solution:
    def climbStairs(self, n: int) -> int:

        front, back = 1, 1

        for _ in range(n - 1):
            temp = front
            front += back
            back = temp
        
        return front

        