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
        if (head == nullptr) return head;
        // Find the length and the end of the listnode
        ListNode* end=head;
        ListNode* prev;
        int count = 0;
        while (end != nullptr) {
            count += 1;
            prev = end;
            end = end->next;
        }

        k = k % count;
        if (k == 0 || count == 1) return head;

        // Find the starting node
        ListNode* dummy = head;
        for (int i=0; i<count-k-1; ++i) {
            dummy = dummy->next;
        }
        ListNode* new_start = dummy->next;
        dummy->next = nullptr;
        prev->next = head;

        return new_start;
    }
};