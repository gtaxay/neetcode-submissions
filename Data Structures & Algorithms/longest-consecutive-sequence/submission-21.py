class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        length = 0
        numSet = set(nums)

        for num in numSet:

            
            if num - 1 not in numSet:
                con = 1
                while num + con in nums:
                    con += 1
                length = max(length, con)
        
        return length
            
        