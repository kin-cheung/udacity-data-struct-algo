Time complexity & space analysis
================================

## Problem 1 : LRU Cache
```
### Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
```

## Explanation

To keep all operations to O(1) time complexity, a map was used to hold cache data and a linked list to keep the recentness of each cache data.

The space complexity of this LRU cache is O(n), where n is the capacity of the cache and the linked list takes up space that is linear to the capacity of the cache.

1. used a map to store cache data. the key of the map is the key to a cache data and the value contains a tuple which consists of the cache data value and a reference to a linked list node, which is used when this cache data is hit
2. used a linked list structure to keep track of the recentness of cache data. One node per cache data. The least recent one is at the head and the most recent one is at the tail.
3. for every cache get and set , map::get and map::set are O(1) 
4. for every cache hit, we mark the cache data to be the most recent, so we move the corresponding linked list node to the tail of the list, that's O(1). 
5. when cache is full, a set() will cause the least recent node, that's the head node, to be deleted and a new node for the new cache data to be linked to the tail of the list, that's O(1)

## Problem 2 : File Recursion
```
Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
```

## Explanation

Since we wanted to find all paths in all sub paths in infinite depth, the time complexity is O(n) where n is the paths and sub paths it can traverse through until it hits the bottom. When it finds a file that matches a given suffix, it appends it to a list and that takes a constant time, O(1).

The space complexity is O(n) linear to the depth of a given directory and its sub-directories for each recursion and the space to store the output.

# Problem 3 : Huffman Coding

```
Huffman Coding

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

    Take a string and determine the relevant frequencies of the characters.
    Build and sort a list of tuples from lowest to highest frequencies.
    Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
    Trim the Huffman Tree (remove the frequencies from the previously built tree).
    Encode the text into its compressed form.
    Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas. 
```

## Explanation

The time complexity is O(nlogn), because a priority queue was used.
The space complexity is O(n), where n is linear to the number of unique characters in a given data:
	- the size of the map that holds frequencies of each unique characters used in (1)
	- the size of the priority queue where the number of nodes is equal to the number of unique characters in the map above
	- the size of the Huffman Tree that is the number of unique characters plus the number of sub-tree roots, that's n + (n - 1)
	- the size of the codeword map that is also equal to the number of unique characters

### Take a string and determine the relevant frequencies of the characters.
1. log(n), a list teration of a string by char, where n is the length of a given string and place a count of each character in a map, similar to radix sort.

### Build and sort a list of tuples from lowest to highest frequencies. 
# Build the Huffman Tree by assigning a binary code to each letter,  using shorter codes for the more frequent letters.
### Trim the Huffman Tree (remove the frequencies from the previously built tree).
2. log(nlogn), used a priority queue from heapq to keep things sorted, where n is the size of the queue, that's the number of distinct characters plus the number of sub-trees
3. log(n), built the Huffman Tree while popping and appending nodes from the priority queue, where n is the size of the queue, and adding nodes to the tree takes constant time, O(1)
4. log(n), built a map to map every distinct character to a corresponding code word while traversing the whole Huffman Tree. n is the size of the tree and adding a value to the map takes n(1)

### Encode the text into its compressed form.
5. log(n), where n is the length of the given string. loop through the string and map each character to a codeword from the codeword map to make up the final output string of 0's and 1's.

### Decode
6. log(n), where n is the length of a given encoded data in binary string format. For each bit in the given string, traverse down the Huffman Tree one node at a time. A mapping character is at a leaf node, when it is found, start from the root again and repeat that until the end of the binary string

# Problem 4 
## Explanation

log(nm), from parent group and recurse down from each sub group to match a given user against a list of users in each group by linear scan, that's log(m)

# Problem 5 : Blockchain

```
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.
```

## Explanation
 
The blockchain was implemented similar to a singly linked list. It takes O(1) time to append a new block and block deletion is not allowed. Using a linked list structure to implement the blockchain came naturally, since we wanted to build a chain where blocks are linked one after another and we wanted to be able to traverse from the genesis node to a given node to verify the chain integrity by validating the hash value in each block that has a domino effect on the whole chain.

The value that goes in the hash of a block is a concatenated string of the timestamp, the data and the hash value of the previous block. Since the hash value from the previous node is included in calculating a hash contaminating a node on a chain will cause hash validation down the chain to fail.

# Problem 6 : Union and Intersection of Two Linked Lists

```
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code. 
```

## Explanation

union() : log(n), where n is the size of the second list. Thought of making use of the size() function to find the bigger list to append the smaller list to but the size function itself is O(n) but it wouldn't help much, unless the size() function is O(1).

intersaction : log(n), where n is the size of the first list or the second list, whichever is larger. A set structure was used for O(1) lookup.