#!/usr/local/bin/python

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q) :
        from collections import deque
        def check_same(ptree,qtree):
            print('check_same')
            if not ptree and not qtree:
                return True
            if (not ptree and qtree) or ( ptree and not qtree):
                return False
            return False if ptree.val != qtree.val else True
        
        deq = deque()
        deq.append((p,q))
        while deq:
            
            print(f'while loop, {deq} \n')
            p1, q1 = deq.popleft()
            if not check_same(p1, q1):
                return False
            if p1.left:
                deq.append((p1.left, q1.left))
            if p1.right:
                deq.append((p1.right, q1.right))
        return True


def main():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    s = Solution()

    print(s.isSameTree(p,q))

if __name__ == '__main__':
    main()
