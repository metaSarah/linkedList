import hashlib
# from sqlite3 import Timestamp
import time

class Block:
    def __init__(self, index, timestamp, content, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.content = content
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
   
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.content).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()
      
M4BlockChain = []

from datetime import datetime
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")
    
M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
def next_block(last_block):
    
    index = last_block.index + 1
    timeStamp = time.localtime()
    content = "this is block {}".format(index)
    previous_hash = last_block.previous_hash

    newBlock = Block(index, timeStamp, content, previous_hash)
    return newBlock
    # pass
    
# append 5 blocks to the blockchain
def app_five(block_list):
    
    # find last block by iterating from genesis block
    # index = 0
    # while (block_list[index])

    # listLength = len(block_list)
    # priorBlockIndex = priorBlock.index
    

    for x in range(0,5):
        priorBlock = block_list[len(block_list) - 1]
        newBlock = next_block(priorBlock)
        block_list.append(newBlock)


    # pass
