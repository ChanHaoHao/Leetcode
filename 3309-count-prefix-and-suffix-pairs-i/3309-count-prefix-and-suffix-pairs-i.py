# Create a Trie and store the zip of the word going forward and reverse and how many times it has gone
# "abc" -> [(a, c), 1], [(b, b), 1], [(c, a), 1]
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1
    
    def count(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # ans = 0
        # for x in range(len(words)):
        #     for y in range(x+1, len(words)):
        #         w1, w2 = words[x], words[y]
        #         l1 = len(words[x])
        #         if w2[:l1]==w1 and w2[-l1:]==w1:
        #             ans += 1
        
        # return ans
        
        ans = 0
        root = Trie()

        for w in reversed(words):
            ans += root.count(w)
            root.add(w)
        
        return ans