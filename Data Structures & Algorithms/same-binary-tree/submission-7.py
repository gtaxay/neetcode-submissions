# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case both dont exist
        if not p and not q:
            return True
        
        # base case only one exists
        elif not p or not q:
            return False
        
        # compare values of roots
        if p.val != q.val:
            return False
        
        # need self because in self 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


        