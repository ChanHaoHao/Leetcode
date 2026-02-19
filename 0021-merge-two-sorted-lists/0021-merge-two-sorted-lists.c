/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;
    dummy.next = NULL;

    struct ListNode* start = &dummy;
    while (list1 != NULL && list2 != NULL) {
        if (list1->val > list2->val) {
            start->next = list2;
            list2 = list2->next;
        }
        else {
            start->next = list1;
            list1 = list1->next;
        }
        start = start->next;
    }

    if (list1 != NULL)
        start->next = list1;
    if (list2 != NULL)
        start->next = list2;
    return dummy.next;
}