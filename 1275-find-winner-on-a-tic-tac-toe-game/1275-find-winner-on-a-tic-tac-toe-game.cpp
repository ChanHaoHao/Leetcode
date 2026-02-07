class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        // There are 8 ways to win, 3 horizontal, 3 vertical, and 2 diagonal
        int status[8] = {0};
        // Let 1 be A, and -1 be B
        int player = 1;

        for (int i=0; i<moves.size(); ++i) {
            int r = moves[i][0];
            int c = moves[i][1];

            status[r] += player;
            status[3 + c] += player;
            if (r == c) status[6] += player;
            if (r+c == 2) status[7] += player;

            if (abs(status[r]) == 3 || abs(status[3 + c]) == 3 || abs(status[6]) == 3 || abs(status[7]) == 3) {
                if (player == 1) return "A";
                return "B";
            }

            player *= -1;
        }    

        if (moves.size() == 9) return "Draw";
        return "Pending";    
    }
};