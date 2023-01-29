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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans=new ListNode(0), tmp=ans;
        int next=0;
        while (l1!=null && l2!=null) {
            int temp=next;
            next=(l1.val+l2.val+next)/10;
            tmp.next=new ListNode(l1.val+l2.val-next*10+temp);
            l1=l1.next;
            l2=l2.next;
            tmp=tmp.next;
        }
        
        while (l1!=null) {
            if (next==0) {
                tmp.next=l1;
                break;
            }
            int temp=next;
            next=(l1.val+next)/10;
            tmp.next=new ListNode(l1.val+temp-next*10);
            l1=l1.next;
            tmp=tmp.next;
        }
        while (l2!=null) {
            if (next==0) {
                tmp.next=l2;
                break;
            }
            int temp=next;
            next=(l2.val+next)/10;
            tmp.next=new ListNode(l2.val+temp-next*10);
            l2=l2.next;
            tmp=tmp.next;
        }
        if (next==1)
            tmp.next=new ListNode(1);
        
        return ans.next;
    }
}