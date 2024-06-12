# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        
        def helper(node, level):
            nonlocal max_depth
            if not node:
                return
            else:
                max_depth = max(level, max_depth)
            
            helper(node.left, level+1)
            helper(node.right, level+1)
        
        helper(root,1)
        return max_depth
