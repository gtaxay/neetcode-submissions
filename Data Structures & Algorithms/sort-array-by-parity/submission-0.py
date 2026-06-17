class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # two pointers
        # front, search 

        front, search = 0, 0


        
        while search < len(nums):
            # if even move to front
            # swap front and search
            # increase front
            if nums[search] % 2 == 0:
                temp = nums[front]
                nums[front] = nums[search]
                nums[search] = temp

                front += 1

            search += 1
        
        return nums


        