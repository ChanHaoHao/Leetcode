int minEatingSpeed(int* piles, int pilesSize, int h) {
    int slow=1, fast=0;

    // find the largest pile
    for (int i=0; i<pilesSize; ++i) {
        if (piles[i] > fast) {
            fast = piles[i];
        }
    }
    int ans = fast;
    while (slow <= fast) {
        int speed = (slow + fast) / 2;
        unsigned int hour = 0;
        for (int i=0; i<pilesSize; ++i) {
            hour += piles[i] / speed;
            if (piles[i] % speed != 0)
                hour++;
        }

        if (hour <= h) {
            ans = fmin(ans, speed);
            fast = speed - 1;
        }
        else {
            slow = speed + 1;
        }
    }

    return ans;
}