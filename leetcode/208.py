class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            currNode = currNode.children[c]
        currNode.isEndOfWord = True 

    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return currNode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True
