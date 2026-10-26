class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # product (multiplication) of all other nums
        # cant use division
        # post and prefix

        # prefix = all multiplication before that value
        prefix = 1
        pre = [1 for i in range(len(nums))]


        for i in range(len(nums)):
            pre[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        post = [1 for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            post[i] = postfix
            postfix = postfix * nums[i]
        
        # combine
        res = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            res[i] = post[i] * pre[i]
        

        return res




        