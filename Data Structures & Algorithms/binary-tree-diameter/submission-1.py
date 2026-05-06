# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

       # return height in sub def
        # make variable of max 
        self.res = 0

        # return height
        def dfs(curr):
            if not curr:
                return 0

            # height of left and right
            right = dfs(curr.right)
            left = dfs(curr.left)

            # max of left to right or current
            self.res = max(self.res, left + right)
            
            # return height
            return 1 + max(right, left)
        
        dfs(root)
        return self.res
        



        