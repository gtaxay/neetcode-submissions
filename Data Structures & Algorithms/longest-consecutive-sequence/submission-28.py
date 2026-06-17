class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # have to start with minumum
        # could go down the line but then repeat
        maximum = 0
        count = 0
        searched = set()
        for n in nums:
            if n in searched:
                continue
            count = 1
            temp = n
            while temp + 1 in nums:
                temp += 1
                count += 1
                searched.add(temp)
            maximum = max(count, maximum)
        
        return maximum


        