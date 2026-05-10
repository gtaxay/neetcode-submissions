class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def backtrack(index, current):
            # base case
            # use condition
            if sum(current) == target:
                res.append(current.copy())
                return 
            # end condition
            if index == len(nums) or sum(current) > target:
                return
            
            current.append(nums[index])
            # dont increase because can repeat the same number
            
            backtrack(index, current)
            # pop and go next
            current.pop()

            backtrack(index + 1, current)


        backtrack(0, [])
        return res
            

            



