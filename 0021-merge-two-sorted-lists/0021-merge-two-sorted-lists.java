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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode ans=null, last=null;
        while (list1!=null || list2!=null) {
            ListNode oldlast=last;
            if (list1==null) {
                last=new ListNode(list2.val, null);
                list2=list2.next;
            }
            else if (list2==null) {
                last=new ListNode(list1.val, null);
                list1=list1.next;
            }
            else if (list1.val>list2.val) {
                last=new ListNode(list2.val, null);
                list2=list2.next;
            }
            else {
                last=new ListNode(list1.val, null);
                list1=list1.next;
            }
            if (ans==null) ans=last;
            else oldlast.next=last;
        }

        return ans;
    }
}