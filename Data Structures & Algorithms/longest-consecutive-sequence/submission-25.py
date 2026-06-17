class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # have to start with minumum
        # could go down the line but then repeat
        maximum = 0
        count = 0
        for n in nums:
            count = 1
            temp = n
            while temp + 1 in nums:
                temp += 1
                count += 1
            maximum = max(count, maximum)
        
        return maximum


        