class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week = [1, 2, 3, 4, 5, 6, 7]
        sum_week = sum(week)
        # Deal with full week
        for i in range(n//7):
            ans += sum_week + i*7

        # Deal with rest of the days
        for i in range(n%7):
            ans += week[i] + n//7

        return ans