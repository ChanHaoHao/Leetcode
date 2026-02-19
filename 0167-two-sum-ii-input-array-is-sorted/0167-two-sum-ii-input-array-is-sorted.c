/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* ans = (int*)calloc(2, sizeof(int));

    for (int i=0; i<numbersSize; ++i) {
        int l=i+1, r=numbersSize-1, remain=target-numbers[i];
        while (l <= r) {
            int mid = (l + r) / 2;
            if (numbers[mid] == remain) {
                ans[0] = i+1;
                ans[1] = mid+1;

                *returnSize = 2;
                return ans;
            }
            else if (numbers[mid] > remain) {
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
    }

    *returnSize = 2;
    return ans;
}