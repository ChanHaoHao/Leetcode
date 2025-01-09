class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        cur = self.root
        
        for x in w:
            if x not in cur.children:
                cur.children[x] = TrieNode()
            cur = cur.children[x]
            cur.count += 1
    
    def count(self, w):
        cur = self.root

        for x in w:
            if x not in cur.children:
                return 0
            cur = cur.children[x]
        
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # ans = 0
        # n = len(pref)
        # for x in words:
        #     if x[:n]==pref:
        #         ans += 1
        
        # return ans
        ans = 0
        root = Trie()

        for w in words:
            root.add(w)
        
        return root.count(pref)