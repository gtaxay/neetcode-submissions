# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # tree
        # dfs
        # what are we tracking:  height
        # condition that no more than 1 difference
        # try helper because returning 2 things

        self.res = True

        def helper(root):

            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            if abs(left - right) > 1:
                self.res = False

            return 1 + max(left,right)

            
            
        
        helper(root)

        return self.res