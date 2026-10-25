class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # appear more than once
        # set compare lenths
        # dictionary check values

        count = {}

        for n in nums:
            if n in count:
                return True
            
            count[n] = 1
        
        return False
        