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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // ListNode left=head, right=head;
        // for (int i=0; i<n; i++)
        //     right=right.next;

        // ListNode ans=new ListNode(), tmp=ans;
        // while (right!=null) {
        //     tmp.next=new ListNode(left.val);
        //     left=left.next;
        //     right=right.next;
        //     tmp=tmp.next;
        // }
        // left=left.next;
        // if (left!=null) {
        //     tmp.next=left;
        // }

        // return ans.next;

        ListNode dummy=new ListNode(0, head);
        ListNode left=dummy, right=head;

        while (n>0 && right!=null) {
            right=right.next;
            n--;
        }

        while (right!=null) {
            left=left.next;
            right=right.next;
        }
        left.next=left.next.next;

        return dummy.next;
    }
}