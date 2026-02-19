/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct {
    int index;
    int temperature;
} Element;

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* ans = (int*)calloc(temperaturesSize, sizeof(int));

    Element* stack = (Element*)malloc(temperaturesSize * sizeof(Element));
    Element last_day;
    last_day.index = temperaturesSize-1;
    last_day.temperature = temperatures[temperaturesSize-1];
    int top = 0;
    stack[0] = last_day;

    for (int i=temperaturesSize-2; i>=0; --i) {
        while (top >= 0 && stack[top].temperature <= temperatures[i]) {
            top--;
        }

        if (top != -1) {
            ans[i] = stack[top].index-i;
        }
        Element curr_day;
        curr_day.index = i;
        curr_day.temperature = temperatures[i];
        stack[++top] = curr_day;
    }

    free(stack);

    *returnSize = temperaturesSize;
    return ans;
}