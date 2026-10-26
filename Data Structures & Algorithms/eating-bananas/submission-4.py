class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # all the eating speeds from 1 to max
        left, right = 1, max(piles)

        # current is max
        res = right

        # binary search
        while left <= right:

            k = (left + right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p) / k)
            
            # if this is better
            if hours <= h:
                res = min(res, k)
                right = k - 1
            # this is worse need faster
            else:
                left = k + 1
        
        return res
        



        