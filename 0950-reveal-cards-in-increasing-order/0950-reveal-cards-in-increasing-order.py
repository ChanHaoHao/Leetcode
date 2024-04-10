class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # thoughts
        # the deck will be filled in this order
        # first pass: 1 _ 2 _ 3 _ 4
        # second pass: 1 _ 2 5 3 _ 4
        # third pass: 1 6 2 5 3 7 4
        # every time you input a number, you will have to skip the next available slot
        n = len(deck)
        result = [0]*n
        skip = False

        indexInDeck = 0
        indexInResult = 0

        deck = sorted(deck)

        while indexInDeck<n:
            # only flipping skip or putting values into result when the current value is 0
            if result[indexInResult]==0:
                if not skip:
                    result[indexInResult] = deck[indexInDeck]
                    indexInDeck+=1
                    skip = True
                else:
                    skip = False

            indexInResult = (indexInResult+1)%n
        return result