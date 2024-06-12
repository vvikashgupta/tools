# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque, defaultdict
        result = defaultdict(list)
        ret_value = []
        deq = deque()
        if not root:
            return result
        deq.append([root,1])
        
        while deq:
            node, level = deq.popleft()
            result[level].append(node.val)
            if node.left:
                deq.append([node.left, level+1])
            if node.right:
                deq.append([node.right, level+1])
        
        for i in range(1,level+1):
            ret_value.append(result[i])
        return ret_value
