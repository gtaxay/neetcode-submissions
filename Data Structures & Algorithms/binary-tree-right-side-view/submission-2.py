# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right = []

        queue = [root]

        while queue:
            level = []
            for _ in range (len(queue)):
                node = queue.pop(0)
                if node:
                    # if this is the fartheset right node
                    if len(queue) == 0:
                        right.append(node.val)
                
                    # order matters, left, then right
                    # append for every node
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
            
            # dont append empty levels
            if level:
                queue = level
        
        return right

                

            


        