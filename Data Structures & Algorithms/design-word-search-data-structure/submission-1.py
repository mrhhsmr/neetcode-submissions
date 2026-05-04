class TrieNode:

    def __init__(self):
        self.kids = [None] * 26
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.kids[i] is None:
                cur.kids[i] = TrieNode()
            cur = cur.kids[i]
        cur.end = True
        

    def search(self, word: str) -> bool:
        def dfs(index, root):
            cur = root

            for i in range(index, len(word)):
                if word[i] == '.':
                    for kid in cur.kids:
                        if kid is not None and dfs(i + 1, kid):
                            return True
                    return False
                else:
                    nextIdx = ord(word[i]) - ord('a')
                    if cur.kids[nextIdx] is None:
                        return False
                    cur = cur.kids[nextIdx]
            return cur.end

        return dfs(0, self.root)
