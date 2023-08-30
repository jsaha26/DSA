/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// class Solution {
// public:
//     void deleteNode(ListNode* node) {
        
//     }
// };

class Solution
{
    public:
    //Function to delete a node without any reference to head pointer.
    void deleteNode(ListNode *del)
    {
       // 'del' => node to be deleted 
       // Instead of deleting that particular node, we can overwrite its data
       // with the data of the next node and then unlink the next node
       del->val = del->next->val;
       del->next = del->next->next;     
    }
};
