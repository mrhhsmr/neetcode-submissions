class TrieNode:
    def __init__(self):
        self.kids = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.kids[i] is None:
                cur.kids[i] = TrieNode()
            cur = cur.kids[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.kids[i] is None:
                return False
            cur = cur.kids[i]
        
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.kids[i] is None:
                return False
            cur = cur.kids[i]
        
        return True
        
        