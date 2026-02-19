/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct {
    int value;
    int count;
} Element;

int compareInt(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int compareFreq(const void* a, const void* b) {
    Element* e1 = (Element*)a;
    Element* e2 = (Element*)b;

    return e2->count - e1->count;
}

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize == 0)
        return NULL;
    
    qsort(nums, numsSize, sizeof(int), compareInt);
    Element* freqMap = malloc(numsSize * sizeof(Element));
    int uniqueCount = 0;

    for (int i=0; i<numsSize; ++i) {
        if (i > 0 && nums[i] == nums[i-1]) {
            freqMap[uniqueCount-1].count++;
        }
        else {
            freqMap[uniqueCount].value = nums[i];
            freqMap[uniqueCount].count = 1;
            uniqueCount++;
        }
    }

    qsort(freqMap, uniqueCount, sizeof(Element), compareFreq);
    int* ans = (int*)malloc(k * sizeof(int));
    *returnSize = k;
    for (int i=0; i<k; ++i) {
        ans[i] = freqMap[i].value;
    }

    free(freqMap);
    return ans;
}