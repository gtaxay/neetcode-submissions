class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # all unique comibations + low bounds is complicatd alg

        res = []

        def backtracking(index, current):

            if index == len(nums) or sum(current) > target:
                return 
            # base case

            if sum(current) == target:
                # append copy bc it changes
                res.append(current.copy())
                return
            
            
            current.append(nums[index])
            # can be same variable
            backtracking(index, current)
            current.pop()
            backtracking(index + 1, current)
        
        backtracking(0, [])
        return res
        