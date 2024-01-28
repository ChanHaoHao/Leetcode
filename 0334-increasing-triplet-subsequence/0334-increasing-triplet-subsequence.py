class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = max(nums)
        num2 = num1

        for x in nums:
            if x<=num1:
                num1 = x
            elif x <= num2:
                num2 = x
            else:
                return True
        return False