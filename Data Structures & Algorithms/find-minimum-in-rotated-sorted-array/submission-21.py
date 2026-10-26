class Solution:
    def findMin(self, nums: List[int]) -> int:

        # rotated array
        # return min
        # find where next value is less

        # two sides to array
        # if mid less than left then in right half, 
        # if mid more than right then in left half, move left to mid

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
            


        