/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int compareChars(const void* a, const void* b) {
    return (*(char*)a - *(char*)b);
}

typedef struct {
    char* sortedKey;
    char** groupStrings;
    int groupSize;
    int groupCapacity;
} AnagramGroup;

char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    if (strsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    AnagramGroup* groups = malloc(strsSize * sizeof(AnagramGroup));
    int numGroups = 0;

    for (int i=0; i<strsSize; ++i) {
        char* sortedStr = strdup(strs[i]);
        qsort(sortedStr, strlen(sortedStr), sizeof(char), compareChars);

        int foundIndex = -1;
        for (int j=0; j<numGroups; ++j) {
            if (strcmp(groups[j].sortedKey, sortedStr) == 0) {
                foundIndex = j;
                break;
            }
        }

        if (foundIndex != -1) {
            if (groups[foundIndex].groupSize == groups[foundIndex].groupCapacity) {
                groups[foundIndex].groupCapacity *= 2;
                groups[foundIndex].groupStrings = realloc(groups[foundIndex].groupStrings, groups[foundIndex].groupCapacity * sizeof(char*));
            }
            groups[foundIndex].groupStrings[groups[foundIndex].groupSize] = strs[i];
            groups[foundIndex].groupSize++;
            free(sortedStr);
        }
        else {
            groups[numGroups].groupCapacity = 4;
            groups[numGroups].sortedKey = sortedStr;
            groups[numGroups].groupStrings = malloc(groups[numGroups].groupCapacity * sizeof(char*));
            groups[numGroups].groupStrings[0] = strs[i];
            groups[numGroups].groupSize = 1;
            numGroups++;
        }
    }

    char*** result = malloc(numGroups * sizeof(char**));
    *returnColumnSizes = malloc(numGroups * sizeof(int));
    *returnSize = numGroups;

    for (int i=0; i<numGroups; ++i) {
        result[i] = groups[i].groupStrings;
        (*returnColumnSizes)[i] = groups[i].groupSize;
        free(groups[i].sortedKey);
    }
    free(groups);

    return result;
}