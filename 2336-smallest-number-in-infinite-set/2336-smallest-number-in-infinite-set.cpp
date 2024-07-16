class SmallestInfiniteSet {
public:
    priority_queue<int, vector<int>, greater<int>> heap;
    unordered_set<int> exist;
    
    SmallestInfiniteSet() {
        for (int i=0; i<1000; i++)
        {
            heap.push(i+1);
            exist.insert(i+1);
        }
    }
    
    int popSmallest() {
        int tmp = heap.top();
        heap.pop();
        exist.erase(tmp);
        return tmp;
    }
    
    void addBack(int num) {
        if (!exist.contains(num))
        {
            heap.push(num);
            exist.insert(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */