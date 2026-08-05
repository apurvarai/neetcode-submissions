# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # dummy=head
        visit=set()
        while head.next is not None:
            visit.add(head)
            head=head.next
            if head in visit:
                return True
        return False
        