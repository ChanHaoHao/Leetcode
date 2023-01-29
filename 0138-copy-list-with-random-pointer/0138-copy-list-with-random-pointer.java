/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> oldCopy=new HashMap<>();
        oldCopy.put(null, null);
        Node cur=head;

        while (cur!=null) {
            Node copy=new Node(cur.val);
            oldCopy.put(cur, copy);
            cur=cur.next;
        }

        cur=head;
        while (cur!=null) {
            Node copy=oldCopy.get(cur);
            copy.next=oldCopy.get(cur.next);
            copy.random=oldCopy.get(cur.random);
            cur=cur.next;
        }
        
        return oldCopy.get(head);
    }
}