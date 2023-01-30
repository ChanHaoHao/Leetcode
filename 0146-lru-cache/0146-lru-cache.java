class LRUCache {

    int cap=0;
    HashMap<Integer, Node> map=new HashMap<>();
    Node left=new Node(0, 0), right=new Node(0, 0);
    public LRUCache(int capacity) {
        cap=capacity;
        left.next=right;
        right.prev=left;
    }

    private void insert(Node node) {
        Node prev=right.prev, next=right;
        prev.next=next.prev=node;
        node.next=next;
        node.prev=prev;
    }

    private void remove(Node node) {
        Node prev=node.prev, next=node.next;
        prev.next=next;
        next.prev=prev;
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            remove(map.get(key));
            insert(map.get(key));
            return map.get(key).val;
        }
        else
            return -1;
    }

    public void put(int key, int value) {
        if (map.containsKey(key))
            remove(map.get(key));
        map.put(key, new Node(key, value));
        insert(map.get(key));

        if (map.size()>cap) {
            Node lru=left.next;
            remove(lru);
            map.remove(lru.key);
        }
    }
}

class Node {
    int key;
    int val;
    Node next;
    Node prev;

    public Node(int key, int val) {
        this.key=key;
        this.val=val;
        this.next=null;
        this.prev=null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */