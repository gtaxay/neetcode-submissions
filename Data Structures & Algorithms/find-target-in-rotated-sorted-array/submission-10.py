class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (right + left)  // 2

            if nums[middle] == target:
                return middle

            #left half
            elif nums[left] <= nums[middle]:
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle
            #right half
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle 
                else:
                    left = middle + 1


        
        return -1
        