class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # two vals that add up to target
        # return index
        # one right answer

        # map with value = index to key
        # see if target - val in nums

        nMap = {}

        for i in range(len(nums)):
            find = target - nums[i]

            if find in nMap:
                return [nMap[find], i]
            
            nMap[nums[i]] = i
        
        


        