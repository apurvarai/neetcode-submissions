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
//finding length of the linked list
if(!head) return nullptr;
        int length=0;
        ListNode* curr=head;
        while(curr){
            curr=curr->next;
            length++;
        }
        cout<<length<<" ";
        ListNode* prev=nullptr;
        curr=head;
        int t=length-n;
        while(t--){
            prev=curr;
            curr=curr->next;
        }
        ListNode* temp=curr->next;
        curr->next=nullptr;
        if(length-n ==0){
            head=temp;
        }
        else{
            prev->next=temp;
        }
        return head;
    }
};
