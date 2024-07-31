class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0]*len(books)

        def helper(i):
            if i==len(books):
                return 0

            if dp[i]!=0:
                return dp[i]
            
            # the helper function will be started with a new shelf everytime
            remaining_width = shelfWidth
            max_height = 0
            dp[i] = float("inf")
            for j in range(i, len(books)):
                book_width, book_height = books[j]
                # if there is not enough space for the book
                if book_width>remaining_width:
                    break
                remaining_width -= book_width
                max_height = max(max_height, book_height)
                # recursively call helper to check whether to put the next book
                # in this shelf or start a new shelf to minimize the shelf
                dp[i] = min(dp[i], helper(j+1)+max_height)
            
            return dp[i]
        
        return helper(0)