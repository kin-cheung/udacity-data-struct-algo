class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.isLeaf = True
    
    def insert(self, char):
        ## Add a child node in this Trie
        node = self.children.get(char, None)
        if node == None :
            self.isLeaf = False
            node = TrieNode()
            self.children[char] = node
        return node
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        if self.isLeaf:
            return [suffix]
        
        output = []        
        for char, child in self.children.items():
            output += child.suffixes(suffix + char)
                
        return output

            
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for c in word :
            node = node.insert(c)
        node.insert('')
            

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for c in prefix :
            node = node.children.get(c, None)
            if node == None :
                break

        return node
        

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "ant", "fun", "ant", "fun", "ant", "fun",
    "hello world, again!!", "hello", "world"
]
for word in wordList:
    MyTrie.insert(word)
    

prefixNode = MyTrie.find('a')
print('\n'.join(prefixNode.suffixes()))
# nt
# nthology
# ntagonist
# ntonym

print(MyTrie.find('z'))
# None

prefixNode = MyTrie.find('trigonometry')
print('\n'.join(prefixNode.suffixes()))
#

prefixNode = MyTrie.find('hel')
print('\n'.join(prefixNode.suffixes()))
# lo world, again!!
# lo

prefixNode = MyTrie.find('wor')
print('\n'.join(prefixNode.suffixes()))
# ld

prefixNode = MyTrie.find('!')
print('\n'.join(prefixNode.suffixes()))
# ! not found