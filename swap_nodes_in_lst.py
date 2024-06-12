# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(lst):
            if not lst or not lst.next:
                return lst
          
            first = lst
            second = lst.next
            first.next = self.swapPairs(lst.next.next)
            second.next = first
            return second
        
        return helper(head)
