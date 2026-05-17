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
    void reorderList(ListNode* head) {

        //Find the middle node using fast and slow pointers
        ListNode* slow=head;
        ListNode* fast=head;

        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
        }
//mid point is at slow pointer right now

//Reverse the second half of the list
        ListNode* curr=slow->next;
        slow->next=nullptr;
        ListNode* prev=nullptr;
while(curr){
    ListNode* temp=curr->next;
    curr->next=prev;

    prev=curr;
    curr=temp;
}

//Merging the two halves of the list

ListNode* first=head;
ListNode* second=prev;

while(second){

ListNode* temp1=first->next;
ListNode* temp2=second->next;

first->next=second;
second->next=temp1;

first=temp1;
second=temp2;

}        


    }
};
