class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # num + num1 - target in map


        nums.sort()
        sol = []

        for i in range(len(nums)):
            front, back = i + 1, len(nums) - 1

            while front < back:
                if nums[i] + nums[front] + nums[back] > 0:
                    back -= 1
                elif nums[i] + nums[front] + nums[back] < 0:
                    front += 1
                else:
                    if [nums[i],nums[front],nums[back]] not in sol:
                        sol.append([nums[i],nums[front],nums[back]])
                    front += 1
        
        return sol
