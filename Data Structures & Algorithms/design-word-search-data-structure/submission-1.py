class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False     
class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.head 
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.is_end
        return dfs(0,self.head)


        
