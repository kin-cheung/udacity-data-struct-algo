import hashlib
      
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __str__(self) :
        s = ''
        if self.timestamp :
            s += str(self.timestamp)
        if self.data :
            s += ':' + self.data
        if self.previous_hash :
            s += ':' + self.previous_hash
        
        return s
    
          
import time

class BlockChain :

    def __init__(self):
        self.genesis  = Block(time.time(), 'genesis', None)
        
    def append(self, data) :
        block = self.genesis 
        while block.next :
            block = block.next
        
        block.next = Block(time.time(), data, block.hash)
    
    def __str__(self) :
        s = ''
        block = self.genesis 
        while block != None :
            s += str(block) + ' -> '
            block = block.next
            
        return s

chain = BlockChain()
block_1 = chain.append('data_1')
block_2 = chain.append('data_2')
block_3 = chain.append('data_3')
print(chain)