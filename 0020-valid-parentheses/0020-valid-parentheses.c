bool isValid(char* s) {
    int n = strlen(s);

    char* stack = (char*)malloc(n * sizeof(char));
    int top = -1;
    for (int i=0; i<n; ++i) {
        char current = s[i];

        if (current == '(' || current == '{' || current == '[') {
            stack[++top] = current;
        }
        else if (current == ')') {
            if (top == -1 || stack[top] != '(')
                return false;
            top--;
        }
        else if (current == '}') {
            if (top == -1 || stack[top] != '{')
                return false;
            top--;
        }
        else if (current == ']') {
            if (top == -1 || stack[top] != '[')
                return false;
            top--;
        }
    }

    return top == -1;
}