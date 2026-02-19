/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;

    while (head != NULL) {
        struct ListNode* tmp = head->next;
        head->next = prev;
        prev = head;
        head = tmp;
    }

    return prev;
}