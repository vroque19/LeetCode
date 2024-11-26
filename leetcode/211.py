class TrieNode:
    def __init__(self, children, isEndOfWord):
        self.children = children
        self.isEndOfWord = isEndOfWord

class WordDictionary:

    def __init__(self):
        self.root = TrieNode({}, False)

    def addWord(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if currNode.children.get(c, None) is None:
                currNode.children[c] = TrieNode({}, False)
            currNode = currNode.children[c]
        currNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        return self.searchHelper(currNode, word)

    def searchHelper(self, currNode, word)->bool:
        i = 0
        for c in word:
            if c == ".":
                found = False
                for char, childNode in currNode.children.items():
                    found = found or (self.searchHelper(childNode, word[1+i:]))
                return found
            elif currNode.children.get(c, None) is None:
                return False
            else:
                currNode = currNode.children[c]
            i += 1
        if currNode.isEndOfWord:
            return True
        return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
