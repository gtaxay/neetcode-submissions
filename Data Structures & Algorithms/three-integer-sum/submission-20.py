class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # triplets
        # need all triplets

        # brute force n^3

        res = []
        nums.sort()

        # two pointers
        for i, n in enumerate(nums):
            front, back = i + 1, len(nums) - 1

            # skip repeats
            if i > 0 and n == nums[i - 1]:
                continue

            while front < back:
                # if target
                if -n == (nums[front] + nums[back]):
                    res.append([n, nums[front], nums[back]])
                    front += 1
                    # dont want repeats
                    while front < back and nums[front] == nums[front - 1]:
                        front +=1
                elif -n > (nums[front] + nums[back]):
                    front += 1
                else:
                    back -= 1
        
        return res
            


            

        


        