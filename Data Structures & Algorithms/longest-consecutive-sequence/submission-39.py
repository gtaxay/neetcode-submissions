class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # longest consecutive (better than 0(n) so no sorting)
        # check if next number in 

        length = 0
        nums = set(nums)

        # how to start with min
        # o(n^2)
        for n in nums:
            # find start 
            if n - 1 not in nums:
                count = 1
                while n + count in nums:
                    count += 1
                length = max(length, count)
        
        return length
        