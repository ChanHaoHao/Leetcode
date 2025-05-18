class Pair:
    def __init__(self, digit_sum, val, id):
        self.digit_sum = digit_sum
        self.val = val
        self.id = id

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        pairs = []
        for i in range(n):
            digit_sum, curr_num = 0, nums[i]
            while curr_num>0:
                digit_sum += curr_num%10
                curr_num = curr_num//10
            pairs.append(Pair(digit_sum, nums[i], i))
        
        pairs.sort(key=lambda x: (x.digit_sum, x.val))

        i, ans = 0, 0
        while i<n:
            if pairs[i].id != i:
                ans += 1
                j = pairs[i].id
                pairs[i], pairs[j] = pairs[j], pairs[i]
            else:
                i += 1
        
        return ans 