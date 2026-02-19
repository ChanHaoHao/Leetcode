


typedef struct {
    int capacity;
    int top;
    int* array;
    int* minarray;
} MinStack;


MinStack* minStackCreate() {
    MinStack* minstack = (MinStack*)malloc(sizeof(MinStack));
    minstack->capacity = 4;
    minstack->top = -1;
    minstack->array = (int*)malloc(minstack->capacity * sizeof(int));
    minstack->minarray = (int*)malloc(minstack->capacity * sizeof(int));

    return minstack;
}

void minStackPush(MinStack* obj, int val) {
    if (obj->top == obj->capacity-1) {
        obj->capacity *= 2;
        obj->array = (int*)realloc(obj->array, obj->capacity * sizeof(int));
        obj->minarray = (int*)realloc(obj->minarray, obj->capacity * sizeof(int));
    }

    obj->array[obj->top+1] = val;
    if (obj->top == -1)
        obj->minarray[obj->top+1] = val;
    else {
        obj->minarray[obj->top+1] = fmin(obj->minarray[obj->top], val);
    }
    obj->top++;
}

void minStackPop(MinStack* obj) {
    if (obj->top == -1) {
        printf("The minStack is empty!\n");
    }
    else {
        obj->top--;
    }
}

int minStackTop(MinStack* obj) {
    return obj->array[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->minarray[obj->top];
}

void minStackFree(MinStack* obj) {
    free(obj->array);
    free(obj->minarray);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/