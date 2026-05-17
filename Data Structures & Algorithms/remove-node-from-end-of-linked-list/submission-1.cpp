/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

//Two Pointers Approach
ListNode* dummy=new ListNode(0,head);

ListNode* left=dummy;
ListNode* right=head;

while(n--){
    right=right->next;
}

while(right){
    left=left->next;
    right=right->next;
}
//current left is at one node before the node we want to remove

ListNode* curr=left->next;
ListNode* temp=curr->next;

left->next=temp;
curr->next=nullptr;


return dummy->next;
    }
};
