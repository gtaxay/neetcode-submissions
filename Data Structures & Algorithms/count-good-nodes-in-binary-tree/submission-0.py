# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good = 0


        def dfs (node, total):
            # base case non existant, end
            if not node:
                return 
            
            # base case this is greater
            if node.val >= total:
                self.good += 1
                total = node.val
            
            dfs(node.left, total)
            dfs(node.right, total)



        dfs(root, root.val)

        return self.good
        