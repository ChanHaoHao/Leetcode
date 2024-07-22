class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        merge = zip(names, heights)

        merge = sorted(merge, key=lambda x: -x[1])

        return [x for x, _ in merge]

        # n = len(names)
        # for x in range(n):
        #     for y in range(x+1, n):
        #         if heights[x]<heights[y]:
        #             tmp = names[x]
        #             names[x] = names[y]
        #             names[y] = tmp
        #             tmp = heights[x]
        #             heights[x] = heights[y]
        #             heights[y] = tmp
        # # print(heights)
        # return names