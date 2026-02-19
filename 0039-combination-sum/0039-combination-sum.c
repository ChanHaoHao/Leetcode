/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void backtrack(int* candidates, int candidatesSize, int i, int remain, int* subset, int subsetSize, int** result, int* returnSize, int** returnColumnSizes) {
    // Answer found
    if (remain == 0) {
        result[*returnSize] = (int*)malloc(subsetSize * sizeof(int));
        memcpy(result[*returnSize], subset, subsetSize * sizeof(int));

        (*returnColumnSizes)[*returnSize] = subsetSize;
        (*returnSize)++;
        return;
    }

    // not a possible solution
    if (remain < 0 || i == candidatesSize)  return;

    subset[subsetSize] = candidates[i];
    backtrack(candidates, candidatesSize, i, remain-candidates[i], subset, subsetSize+1, result, returnSize, returnColumnSizes);
    backtrack(candidates, candidatesSize, i+1, remain, subset, subsetSize, result, returnSize, returnColumnSizes);
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    int** result = (int**)malloc(150 * sizeof(int*));
    *returnColumnSizes = (int*)malloc(150 * sizeof(int));
    *returnSize = 0;

    int* subset = (int*)malloc(target * sizeof(int));
    int subsetSize = 0;

    backtrack(candidates, candidatesSize, 0, target, subset, subsetSize, result, returnSize, returnColumnSizes);
    free(subset);
    
    return result;
}