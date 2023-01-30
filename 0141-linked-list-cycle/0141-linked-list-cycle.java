/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // HashMap<ListNode, ListNode> map=new HashMap<>();

        // while (head!=null) {
        //     if (map.containsKey(head) && map.get(head).next==head.next)
        //         return true;
        //     map.put(head, head);
        //     head=head.next;
        // }

        // return false;
        ListNode fast=head, slow=head;
        while (fast!=null && fast.next!=null) {
            slow=slow.next;
            fast=fast.next.next;
            if (fast==slow)
                return true;
        }

        return false;
    }
}