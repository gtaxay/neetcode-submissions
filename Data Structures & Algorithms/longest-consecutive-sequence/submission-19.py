class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        longest = 0

        numSet = set(nums)

        # don't ahve to sort if looking at total
        

        for n in numSet:
            # only count if n is the first of the count
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)

        
        return longest
            

        