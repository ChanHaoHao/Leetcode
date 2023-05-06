class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words=sorted(words)

        words=Counter(words)

        return [word for word, _ in words.most_common(k)]