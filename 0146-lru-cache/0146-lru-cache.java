import java.util.HashMap;

class LRUCache {

    private class Node {
        int key;
        int value;
        Node prev;
        Node next;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private HashMap<Integer, Node> cache;
    private int capacity;
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        
        // Dummy head and tail nodes for the doubly linked list
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) {
            return -1;  // Return -1 if the key does not exist
        }
        
        // Move the accessed node to the head (most recently used)
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = cache.get(key);
        
        if (node != null) {
            // Key exists, update value and move it to the head
            node.value = value;
            moveToHead(node);
        } else {
            // Key doesn't exist, create a new node
            Node newNode = new Node(key, value);
            cache.put(key, newNode);
            addNode(newNode);
            
            if (cache.size() > capacity) {
                // Cache is over capacity, remove the least recently used (LRU) node
                Node tailNode = popTail();
                cache.remove(tailNode.key);
            }
        }
    }

    private void addNode(Node node) {
        // Add new node right after the head
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(Node node) {
        // Remove an existing node from the linked list
        Node prevNode = node.prev;
        Node nextNode = node.next;

        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }

    private void moveToHead(Node node) {
        // Move a node to the head (most recently used)
        removeNode(node);
        addNode(node);
    }

    private Node popTail() {
        // Remove the least recently used (LRU) node, which is right before the tail
        Node res = tail.prev;
        removeNode(res);
        return res;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
