# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev=head
        curr=head.next
        temp=curr.next

        while temp is not None:
            curr.next=prev
            if prev==head:
                prev.next=None
            prev=curr
            curr=temp
            temp=temp.next
        curr.next=prev
        if prev==head:
            prev.next=None
        return curr
        