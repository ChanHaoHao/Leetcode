


typedef struct {
    int capacity;
    int top;
    int* minstack;
    int* stack;
} MinStack;


MinStack* minStackCreate() {
    MinStack* minstack = (MinStack*)malloc(sizeof(MinStack));
    minstack->capacity = 10;
    minstack->top = -1;
    minstack->minstack = (int*)malloc(minstack->capacity * sizeof(int));
    minstack->stack = (int*)malloc(minstack->capacity * sizeof(int));

    return minstack;
}

void minStackPush(MinStack* obj, int val) {
    // Check if the stack is full
    if (obj->top == obj->capacity-1) {
        obj->capacity *= 2;
        obj->minstack = (int*)realloc(obj->minstack, obj->capacity * sizeof(int));
        obj->stack = (int*)realloc(obj->stack, obj->capacity * sizeof(int));
    }
    obj->stack[obj->top+1] = val;
    // if the stack is empty
    if (obj->top == -1) {
        obj->minstack[obj->top+1] = val;
    }
    else {
        obj->minstack[obj->top+1] = fmin(obj->minstack[obj->top], val);
    }
    obj->top++;
}

void minStackPop(MinStack* obj) {
    if (obj->top == -1) {
        printf("The stack is empty!\n");
        return;
    }

    obj->top--;
}

int minStackTop(MinStack* obj) {
    if (obj->top == -1)
        return INT_MIN;
    return obj->stack[obj->top];
}

int minStackGetMin(MinStack* obj) {
    if (obj->top == -1)
        return INT_MIN;
    return obj->minstack[obj->top];
}

void minStackFree(MinStack* obj) {
    free(obj->minstack);
    free(obj->stack);
    free(obj);
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