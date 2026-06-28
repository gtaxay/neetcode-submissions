class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # get max rate from piles
        # min rate is 1
        l, r = 1, max(piles)
        sol = r


        while l <= r:
            
            rate = (l + r) // 2
            time = 0
            for b in piles:
                time += math.ceil(float(b) / rate)
            
            if time <= h:
                sol = rate
                r = rate - 1
            else:
                l = rate + 1



        
        return sol






        