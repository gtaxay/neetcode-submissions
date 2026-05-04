# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if neither exists they are the same
        if not p and not q:
            return True
        
        # if one doesnt exist or they do not have the same value they are different
        if not p or not q or p.val != q.val:
            return False

        
         

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        



        