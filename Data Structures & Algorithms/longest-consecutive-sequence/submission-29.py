class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # length
        # dont include if no before
        length = 0
        for n in nums:
            count = 1
            if n - 1 not in nums:
                while n + count in nums:
                    count += 1

            length = max(length, count)
                
        return length