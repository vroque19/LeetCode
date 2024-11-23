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
    if currNode.children.isEmpty {
      currNode.isEndOfWord = true
    }
  }

  func printWords() {
    dfs(node: root)
  }
  func dfs(node: TrieNode) {
    for (char, childNode) in node.children {
      if childNode.isEndOfWord {
        print(char)
      } else {
        print(char, terminator: "")
      }
      dfs(node: childNode)
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
    print("completed BFS!")
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
}

func main() {
  let prefixTree = Trie()
  prefixTree.insertWord(word: "hey")
  prefixTree.insertWord(word: "goodbye")
  prefixTree.insertWord(word: "no")
  prefixTree.insertWord(word: "good")
  print("printing words in our trie:")
  prefixTree.printWords()
  print()
  var _ = prefixTree.isPrefix(word: "go")
  var _ = prefixTree.isWord(word: "go")
  var _ = prefixTree.isWord(word: "goodbye")
}

main()
