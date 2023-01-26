/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        ListNode slow=head, fast=head.next;

        while (fast!=null && fast.next!=null) {
            slow=slow.next;
            fast=fast.next.next;
        }

        ListNode secondPart=slow.next, prev=null;
        slow.next=null;

        while (secondPart!=null) {
            ListNode tmp=secondPart.next;
            secondPart.next=prev;
            prev=secondPart;
            secondPart=tmp;
        }

        ListNode firstPart=head;
        secondPart=prev;
        while (secondPart!=null) {
            ListNode tmp1=firstPart.next, tmp2=secondPart.next;
            firstPart.next=secondPart;
            secondPart.next=tmp1;
            firstPart=tmp1;
            secondPart=tmp2;
        }
    }
}