# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        lenl=head
        while lenl:
            lenl=lenl.next
            k+=1
        if k==1:
            head=None
            return head
        cnt=k-n+1
        if cnt==1:
            return head.next
        prev,curr=head,head
        while cnt>1:
            prev=curr
            curr=curr.next
            cnt-=1
        prev.next=curr.next
        return head
        