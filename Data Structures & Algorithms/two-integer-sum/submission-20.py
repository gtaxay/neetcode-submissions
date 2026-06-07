class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # find target value

        found = {}

        for i in range(len(nums)):
            if target - nums[i] in found and found[target - nums[i]] != i:
                return [found[target - nums[i]], i]        
            found[nums[i]] = i
        
    
    


        