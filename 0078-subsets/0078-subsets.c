/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void backtrack(int* nums, int numsSize, int i, int* subset, int subsetSize, int** result, int* returnSize, int** returnColSize) {
    if (i == numsSize) {
        result[*returnSize] = (int*)malloc(subsetSize * sizeof(int));
        memcpy(result[*returnSize], subset, subsetSize * sizeof(int));

        (*returnColSize)[*returnSize] = subsetSize;
        (*returnSize)++;
        return;
    }

    subset[subsetSize] = nums[i];
    backtrack(nums, numsSize, i+1, subset, subsetSize+1, result, returnSize, returnColSize);
    backtrack(nums, numsSize, i+1, subset, subsetSize, result, returnSize, returnColSize);
}

int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int* subset = (int*)malloc(numsSize * sizeof(int));
    int subsetSize = 0;
    int totalSubset = 1 << numsSize;
    *returnSize = 0;
    int** result = (int**)malloc(totalSubset * sizeof(int*));
    *returnColumnSizes = (int*)malloc(totalSubset * sizeof(int));

    backtrack(nums, numsSize, 0, subset, subsetSize, result, returnSize, returnColumnSizes);
    free(subset);

    return result;
}