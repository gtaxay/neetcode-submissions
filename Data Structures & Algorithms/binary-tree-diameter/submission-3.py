# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # pattern: tree
        # alg: DFS
        # what are we tracking: length of path (bottom to current)
        # need to find max - global variable

        self.longest = 0

        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            self.longest = max(left + right, self.longest)

            return 1 + max(left, right)
        




        helper(root)
        
        return self.longest