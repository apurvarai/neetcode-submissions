# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        k1,k2=0,0
        h1,h2=l1,l2
        while h1:
            k1+=1
            h1=h1.next
        while h2:
            k2+=1
            h2=h2.next
        if k1<k2:
            l1,l2=l2,l1
        carry=0
        h1,h2=l1,l2
        while h1 and h2:
            h1.val=h1.val+h2.val+carry
            carry=1 if h1.val>9 else 0
            h1.val=h1.val%10
            h1=h1.next
            h2=h2.next
        while h1:
            h1.val=h1.val+carry
            carry=1 if h1.val>9 else 0
            h1.val=h1.val%10
            h1=h1.next
        if carry:
            h1=l1
            while h1.next:
                h1=h1.next
            h1.next=ListNode(carry,None)
        return l1



        