# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # pattern: tree
        # DFS or BFS (Going DFS)
        # What are we tracking: equivelance (true or false)
        # method compare each sub-tree (helper)



        def subTree(one, two):

        # base case: both don't exist
            if not one and not two:
                return True
            
        # base case: one doesn't exist
            if not one or not two or not(one.val == two.val):
                return False
        
            return subTree(one.left,two.left) and subTree(one.right,two.right)
        





        return subTree(p,q)

        