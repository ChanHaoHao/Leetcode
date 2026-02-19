/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* ans = calloc(2, sizeof(int));
    *returnSize = 2;

    int l=0, r=numbersSize-1;
    while (l < r) {
        int sum = numbers[l] + numbers[r];
        if (sum == target) {
            ans[0] = l+1;
            ans[1] = r+1;

            return ans;
        }
        else if (sum > target) {
            r--;
        }
        else {
            l++;
        }
    }

    return ans;
}