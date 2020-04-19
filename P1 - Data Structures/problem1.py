class Node(object) :
    def __init__(self, value, parent = None) :
        self.value = value
        self.parent = parent
        self.child = None
    
    def setChild(self, node) :
        self.child = node
        
    def setParent(self, node) :
        self.parent = node
        
    def delete(self) :
        if self.parent != None :
            self.parent.setChild(self.child)
            self.child.setParent(self.parent)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.root = Node(None)
        self.tail = self.root
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self.cache.get(key, -1)
        if value == -1 :
            return -1
        else:
            value[1].delete()
            self.tail.setChild(Node(key, self.tail))
            self.tail = self.tail.child
            return value[0]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.cache :
            if len(self.cache) == self.capacity :
                key_to_delete = self.root.child.value
                self.root.child.delete()
                del self.cache[key_to_delete]
                
            self.tail.setChild(Node(key, self.tail))
            self.tail = self.tail.child
            self.cache[key] = [value, self.tail]    
        

our_cache = LRU_Cache(5)

print(our_cache.get(1))       # returns -1
#-1

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
# 1
print(our_cache.get(2))       # returns 2
# 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
# 9

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
