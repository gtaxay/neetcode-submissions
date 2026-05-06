# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS use queue

        res = []
        q = []
        q.append(root)

        # while there is something in the que:
        while q:
            level = []

            # go over each node at level
            for i in range(len(q)):
                node = q.pop(0)

                # add node to level and add children to queue
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
            

        return res

        