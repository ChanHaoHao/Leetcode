class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // the greater<int> turns the heap from max_heap into min_heap
        // the greater<int> can be modified into self-defined cmp
        priority_queue<int, vector<int>, greater<int>> heap;

        for (int i=0; i<k; i++)
        {
            heap.push(nums[i]);
        }
        for (int i=k; i<nums.size(); i++)
        {
            heap.push(nums[i]);
            heap.pop();
        }

        return heap.top();
    }
};