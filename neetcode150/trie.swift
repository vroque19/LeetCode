import Foundation

class TrieNode {
  var children: [Character: TrieNode]
  var isEndOfWord: Bool

  init() {
    self.children = [:]
    self.isEndOfWord = false
  }
}

class Trie {
  private let root: TrieNode
  init() {
    root = TrieNode()
  }

  func insertWord(word: String) {
    var currNode = root
    for char in word {
      if currNode.children[char] == nil {
        currNode.children[char] = TrieNode()
      }
      currNode = currNode.children[char]! // forcibly access the optional val
    }
    currNode.isEndOfWord = true
  }

  func printWords() {
    let currNode: TrieNode = root
    printWord(prefix: "", currNode: currNode)
  }

  func printWord(prefix: String, currNode: TrieNode) {
    if currNode.isEndOfWord {
      print(prefix)
    }
    for (char, childNode) in currNode.children {
      printWord(prefix: prefix + String(char), currNode: childNode)
    }
  }

  func bfs() {
    var queue: [TrieNode] = []
    queue.append(root)
    while !queue.isEmpty {
      let currNode = queue.removeFirst()
      for (char, node) in currNode.children {
        print("found \(char)")
        queue.append(node)
      }
    }
  }

  func isPrefix(word: String) -> Bool {
      var currNode = root
      for char in word {
        if !isChild(node: currNode, currChar: char) {
          print("did not find \"\(word)\"\n")
          return false
        }
        currNode = currNode.children[char]!
      }
      print("found \"\(word)\"\n")
      return true
    }

  func isChild(node: TrieNode, currChar: Character) -> Bool {
      return node.children[currChar] != nil
  }

  func isWord(word: String) -> Bool  {
    var currNode = root
    for char in word {
      if !isChild(node: currNode, currChar: char) {
          print("\"\(word)\" is not a valid word\n")
          return false
        }
      currNode = currNode.children[char]!
    }
    if currNode.isEndOfWord {
      print("\(word) is a valid word")
      return true
    }
    print("\"\(word)\" is not a valid word\n")
    return false
  }

  func insertWords(words: [String] = []) {
    for word in words {
      insertWord(word: word)
    }
  }
  func findWordsGivenPrefix(prefix: String) -> [String] {
      var validWords: [String] = []
      if !isPrefix(word: prefix) {
          return []
      }
      var currNode: TrieNode = root
      for c in prefix {
          currNode = currNode.children[c]!
      }
      validWords = addValidWords(currNode: currNode, prefix: prefix)
      print("Printing all words with prefix \"\(prefix)\"...")
      return validWords
  }

  func addValidWords(currNode: TrieNode, prefix: String) -> [String] {
      var words: [String] = []
      if currNode.isEndOfWord {
          words.append(prefix)
      }
      for (char, childNode) in currNode.children {
          words += addValidWords(currNode: childNode, prefix: prefix + String(char))
      }
      return words
  }

}



func main() {
  let prefixTree = Trie()
  let list: [String] = ["go", "and", "good", "goal", "gone", "get"]
  prefixTree.insertWords(words: list)
  let found = prefixTree.findWordsGivenPrefix(prefix: "go")
  for word in found {
    print(word)
  }
  
  // prefixTree.printWords()
  print()
  var _ = prefixTree.isPrefix(word: "go")
  var _ = prefixTree.isWord(word: "go")
  var _ = prefixTree.isWord(word: "goodbye")
}

main()
