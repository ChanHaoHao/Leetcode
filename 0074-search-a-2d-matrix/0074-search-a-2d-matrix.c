bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int top=0, bot=matrixSize-1, COL=matrixColSize[0];
    while (top <= bot) {
        int mid = (top + bot) / 2;
        
        if (matrix[mid][0] <= target && target <= matrix[mid][COL-1]) {
            break;
        }
        else if (matrix[mid][0] > target) {
            bot = mid - 1;
        }
        else {
            top = mid + 1;
        }
    }

    if (top > bot)
        return false;
    
    int targetRow = (top + bot) / 2, l=0, r=COL-1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (matrix[targetRow][mid] == target)
            return true;
        else if (matrix[targetRow][mid] < target)
            l = mid + 1;
        else
            r = mid - 1;
    }

    return false;
}