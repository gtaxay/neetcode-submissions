class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # defualt, 1 for nothing 
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        sol = [1 for i in range(len(nums))]

        # first value has no pre or post fix
        # prefix = nums[cur - 1] * prefix[cur - 1]
        # postfix = 

        # calc pre
        for i in range(1, len(nums)):
            print(i)
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        # calc post
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        for i in range(len(nums)):
            sol[i] = prefix[i] * postfix[i]
        
        return sol
            




        