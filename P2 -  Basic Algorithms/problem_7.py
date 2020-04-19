# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for part in parts[:-1] :
            node = node.insert(part)
        node.insert(parts[-1], handler)

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for part in parts :
            node = node.children.get(part, None)
            if node == None :
                break
                
        if node == None:
            return None
        else :
            return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.isLeaf = True
        self.handler = None

    def insert(self, part, handler = None):
        # Insert the node as before
        node = self.children.get(part, None)
        if node == None :
            new_node = RouteTrieNode()
            if handler != None :
                new_node.handler = handler
            self.children[part] = new_node
            node = new_node
            
        return node

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie()
        self.add_handler("/", root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.trie.find(self.split_path(path))
        if handler == None :
            return self.not_found_handler
        else :
            return handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(path) > 0 :
            while len(path) > 1 and path[-1] == '/' :
                path = path[:-1]
            return path.split('/') 
        else :
            return []
        
        
# Here are some test cases and expected outputs you can use to test your implementation
t = RouteTrie()
t.insert('/home/page1'.split('/'), 'page1_handler')
t.insert('/home/page1/part2'.split('/'), 'page2_handler')

print(t.find('/home/page1'.split('/')))
# page1_handler

print(t.find('/home/page1/part2'.split('/')))
# page2_handler

print(t.find('/home'.split('/')))
# None

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) 
# root handler
print(router.lookup("////")) 
# root handler
print(router.lookup(""))
# not found handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/about")) 
# about handler
print(router.lookup("/home/about/")) 
# about handler
print(router.lookup("/home/about/me"))
# not found handler
print(router.lookup("/home/me/about/")) 
# not found handler