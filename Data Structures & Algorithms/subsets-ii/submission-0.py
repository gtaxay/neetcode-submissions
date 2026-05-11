class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(index, current):
            # stop case
            if index == len(nums):
                res.append(current.copy())
                return
            
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1, current)
        
        backtrack(0, [])
        return res