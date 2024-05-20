class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def find_subset(nums, pointer, curr):
            self.ans += curr^nums[pointer]

            # got inspired by this
            # https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/
            if pointer+1<len(nums):
                # this includes the current element
                find_subset(nums, pointer+1, curr^nums[pointer])
                # this excludes the current element
                find_subset(nums, pointer+1, curr)

        find_subset(nums, 0, 0)
        return self.ans