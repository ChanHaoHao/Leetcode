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
    ListNode* rotateRight(ListNode* head, int k) {
        // If the head is empty or the lenght of the linked list is 1
        if (head == nullptr || head->next == nullptr) return head;
        // Find the length and the end of the listnode
        ListNode* end=head;
        int count = 1;
        while (end->next != nullptr) {
            count += 1;
            end = end->next;
        }

        k = k % count;
        // If no rotation is needed
        if (k == 0) return head;

        // Find the starting node
        ListNode* dummy = head;
        for (int i=0; i<count-k-1; ++i) {
            dummy = dummy->next;
        }
        ListNode* new_start = dummy->next;
        dummy->next = nullptr;
        end->next = head;

        return new_start;
    }
};