class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # loop through starting if there is no previous element
        # while .. + len keep going

        streak = 0

        for num in nums:

            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                streak = max(streak,length)
        
        return streak
        