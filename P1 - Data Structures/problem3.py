import sys
import heapq

class BT_Node(object) :    
    def __init__(self, freq, char = None, left = None, right = None) :
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return True
    
    def __str__(self):
        return 'BT_Node(%d): %s, %s/%s' % (self.freq, self.char, self.left if self.left != None else None, self.right if self.right != None else None)
        
    def __repr__(self):
        return self.__str__()

def build_codewords(root) :
    codewords = {}
    stack = []
    node_tuple = (root, '') if root else None
    while node_tuple != None :
        bt_node = node_tuple[0]
        codeword = node_tuple[1]
        
        if bt_node.left != None :
            stack.append((bt_node.left, codeword + '0'))
        if bt_node.right != None :
            stack.append((bt_node.right, codeword + '1'))
        
        if bt_node.left == None and bt_node.right == None :
            codewords[bt_node.char] = codeword
    
        node_tuple = stack.pop() if len(stack) > 0 else None
    
    return codewords

def build_tree(q) :
    tree = None
    if len(q) == 1 :
        right = heapq.heappop(q)
        tree = BT_Node(right[0], None, None, right[1]) 
    else :    
        while len(q) > 1 :
            left = heapq.heappop(q)
            right = heapq.heappop(q)
            freq = left[0] + right[0]
            tree = BT_Node(freq, None, left[1], right[1]) 
            heapq.heappush(q, (freq, tree))
    return tree

def determine_frequencies(data) :
    freqs = {}
    for c in data :
        freq = freqs.get(c, 0)
        freqs[c] = freq + 1
    return freqs

def build_priority_q(freqs) :
    q = []
    for char, freq in freqs.items() :
        heapq.heappush(q, (freq, BT_Node(freq, char)))
    return q

def huffman_encoding(data):
    # Take a string and determine the relevant frequencies of the characters.
    freqs = determine_frequencies(data)
        
    # Build and sort a list of tuples from lowest to highest frequencies. 
    q = build_priority_q(freqs)
    
    # Build the Huffman Tree by assigning a binary code to each letter, 
    # using shorter codes for the more frequent letters.
    # Trim the Huffman Tree (remove the frequencies from the previously built tree).
    tree = build_tree(q)    
    codewords = build_codewords(tree)
    
    # Encode the text into its compressed form.
    binary_str = ''.join([codewords[char] for char in data])        
    
    return binary_str, tree

def huffman_decoding(data, tree):
    decoded_data = ''
    node = tree
    for b in data :
        node = node.left if b == '0' else node.right    
        if node.char != None :
            decoded_data += node.char
            node = tree
    return decoded_data

# test cases

encoded_data_test_1, tree_test_1 = huffman_encoding("The bird is the word")
print (sys.getsizeof(int(encoded_data_test_1, base=2)))
# 36
print (encoded_data_test_1)
# 0111101110111101101000000101111001100011100111011101111110010010000010
print (huffman_decoding(encoded_data_test_1, tree_test_1))
# The bird is the word

encoded_data_test_2, tree_test_2 = huffman_encoding("a")
print (sys.getsizeof(int(encoded_data_test_2, base=2)))
# 28
print (encoded_data_test_2)
# 1
print (huffman_decoding(encoded_data_test_2, tree_test_2))
# a

encoded_data_test_3, tree_test_3 = huffman_encoding("")
print (encoded_data_test_3)
# 
print (huffman_decoding(encoded_data_test_3, tree_test_3))
# 