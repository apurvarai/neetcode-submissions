# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=head
        curr=head.next
        new=curr.next
        while new is not None:
            curr.next=prev
            if prev==head:
                prev.next=None
            # prev.next=None
            prev=curr
            curr=new
            new=new.next
        curr.next=prev
        if prev==head:
            prev.next=None
        # prev.next=None
        return curr