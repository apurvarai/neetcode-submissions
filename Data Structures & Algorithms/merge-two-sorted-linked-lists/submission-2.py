# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        l=[]
        while list1 and list2:
            # node=ListNode()
            if list1.val<list2.val:
                # node.val=list1.val
                l.append(list1.val)
                list1=list1.next
            else:
                # node.val=list2.val
                l.append(list2.val)
                list2=list2.next
        while list1:
            # node.val=list1.val
            l.append(list1.val)
            list1=list1.next
        while list2:
            # node.val=list2.val
            l.append(list2.val)
            list2=list2.next
        head=ListNode(l[0])
        curr=head
     
        for i in range(1,len(l)):
            node=ListNode(l[i])
            # curr=node
            curr.next=node
            node.val=l[i]
            curr=node
        return head

        