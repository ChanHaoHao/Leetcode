class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for operation in operations:
            if '+' in operation:
                ans += 1
            else:
                ans -= 1
        return ans