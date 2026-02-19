typedef struct {
    int r;
    int c;
} Coord;

typedef struct {
    int capacity;
    Coord* storage;
    int top;
} Stack;

Coord* createCoord(int r, int c) {
    Coord* coord = (Coord*)malloc(sizeof(Coord));
    coord->r = r;
    coord->c = c;

    return coord;
}

Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->storage = (Coord*)malloc(stack->capacity * sizeof(Coord));
    stack->top = -1;

    return stack;
}

void pushStack(Stack* stack, Coord coord) {
    if (stack->top == stack->capacity-1) {
        stack->capacity *= 2;
        stack->storage = (Coord*)realloc(stack->storage, stack->capacity * sizeof(Coord));
    }
    stack->storage[++stack->top] = coord;
}

Coord popStack(Stack* stack) {
    if (stack->top == -1) {
        Coord* dummy = createCoord(-1, -1);
        return *dummy;
    }
    return stack->storage[stack->top--];
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int ans = 0;
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    for (int r=0; r<gridSize; ++r) {
        for (int c=0; c<gridColSize[r]; ++c) {
            if (grid[r][c] == '1') {
                Stack* stack = createStack(10);
                Coord* coord = createCoord(r, c);
                grid[r][c] = '0';
                pushStack(stack, *coord);

                while (stack->top != -1) {
                    Coord curr = popStack(stack);

                    for (int i=0; i<4; ++i) {
                        Coord* nxt = createCoord(curr.r+dr[i], curr.c+dc[i]);
                        if (0 <= nxt->r && nxt->r < gridSize && 0 <= nxt->c && nxt->c < gridColSize[r] && grid[nxt->r][nxt->c]=='1') {
                            grid[nxt->r][nxt->c] = '0';
                            pushStack(stack, *nxt);
                        }

                        free(nxt);
                    }

                }

                free(coord);
                free(stack);
                ans++;
            }
        }
    }

    return ans;
}