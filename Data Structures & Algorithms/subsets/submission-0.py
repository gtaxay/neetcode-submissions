class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(index, current):
            # leaf
            if index == len(nums):
                # return copy of current
                res.append(current.copy())
                return
            
            current.append(nums[index])
            helper(index + 1, current)

            # backtrack
            current.pop()
            helper(index + 1, current)
        
        helper(0, [])
        return res
            

        