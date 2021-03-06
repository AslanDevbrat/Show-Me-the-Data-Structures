# -*- coding: utf-8 -*-
"""Problem 5: Blockchain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-7HEQtC2SpPs-WcHCSrWvwG078UczZhk
"""

import hashlib
from time import gmtime,strftime
import time
import json
from hashlib import sha256

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        #print('Node called')
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

class Block(Node):

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        #print('Block __init__ called')
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def calc_hash(self):
      #print('calc_hash called')
      """
      A function that return the hash of the block contents.
       """
      block_string = json.dumps(self.__dict__, sort_keys=True)
      return sha256(block_string.encode()).hexdigest()
class Blockchain:
  # difficult of our proof of work algorithm
  difficulty = 2


  def __init__(self):
    #print('Blockchain called called')
    """Constructor for the Blockchain Class.
    """
    self.chain =[]
    self.unconfirmed_transactions = []
    self.create_genesis_block()

  def create_genesis_block(self):
    """
    A function to generate genesis block and append it to the chain.
    THe block has index 0, previour_hash as - and a valid Hash 
    """
    #print('Bcreate_geneisis  called')
    genesis_block = Block(0, [], 0, "0")
    genesis_block.hash = genesis_block.calc_hash()
    self.chain.append(genesis_block)

  @property
  def last_block(self):
        """
        A quick pythonic way to retrieve the most recent block in the chain. Note that
        the chain will always consist of at least one block (i.e., genesis block)
        """
        #print('last_block called')
        return self.chain[-1]

  def add_block(self,block , proof):
    """
    A function that adds the blocks to the chain after verification .
    Which inculdes:
    - Checking if the proof is valid
    - The previous _hash referred in the block and the hash of latest block
        in the chain match.
    """
    #print('add_block called')
    previous_hash = self.last_block.hash

    if previous_hash != block.previous_hash:
      return False

    if not Blockchain.is_valid_proof(block,proof):
      return False
    
    block.hash = proof
    self.chain.append(block)
  
    return True

  @staticmethod
  def proof_of_work(block):
    """
    Function that tries diffferent value of nonce to get a hash to get a
    hash that satisies our difficulty criteria.
    """
    #print('proof_of_work called')

    block.nonce = 0

    computed_hash =block.calc_hash()

    while not computed_hash.startswith('0'*Blockchain.difficulty):
      block.nonce +=1
      computed_hash = block.calc_hash()

    return computed_hash

  def add_new_transaction(self,transaction):
    #print('add_new_tranction called')
    self.unconfirmed_transactions.append(transaction)

  @classmethod
  def is_valid_proof(cls, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.calc_hash())


  @classmethod
  def check_chain_validity(cls,chain):
    #print('check_chain_validity called')
    result = Trueprevious_hash = '0'

    for block in chain:
      block_hash = block.hash
      """
      remove the hash field to recompute the hash again using 'calc_hash,
      method
      """

      delattr(block,"hash")

      if not cls.is_valid_proof(block, block_hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break
      block.hash, previous_hash = block_hash, block_hash
      return result     

  def mine(self):
    """
    This function serves as an inteface to add the pending
    transaction to the blockcjhain by adding them to the block
    and figuring out proof of work
    """     
   # print('mine called')

    if not self.unconfirmed_transactions:
      return False
    last_block = self.last_block

    new_block = Block(index=last_block.index+1,
                      transactions=self.unconfirmed_transactions,
                          timestamp=time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),
                          previous_hash=last_block.hash)
    proof = self.proof_of_work(new_block)
    self.add_block(new_block,proof)
    self.unconfirmed_transactions = []

    return True

# Test 1
input_data =['I','have ','Implemented','Blockchain','using','LinkedList']
test_blockchain = Blockchain()
for item in input_data:
  test_blockchain.add_new_transaction(item)
  test_blockchain.mine()
list_ = LinkedList(test_blockchain.chain)

node = list_.head
while node:
  block = node.value
  print('Index = ',block.index)
  print('Data = ',block.transactions)
  print('Timestamp =',block.timestamp)
  print('Previous-Hash =',block.previous_hash)
  print('Current-Hash',block.hash)
  print('Nonce',block.nonce)
  print('------------------------------------------------------------------------------------------------------------')
  node  = node.next

# Test 2
input_data =list()
test_blockchain = Blockchain()
for item in input_data:
  test_blockchain.add_new_transaction(item)
  test_blockchain.mine()
list_ = LinkedList(test_blockchain.chain)

node = list_.head
while node:
  block = node.value
  print('Index = ',block.index)
  print('Data = ',block.transactions)
  print('Timestamp =',block.timestamp)
  print('Previous-Hash =',block.previous_hash)
  print('Current-Hash',block.hash)
  print('Nonce',block.nonce)
  print('------------------------------------------------------------------------------------------------------------')
  node  = node.next

# Test 3
input_data =['I studied','Blockchain','in','My','College']
test_blockchain = Blockchain()
for item in input_data:
  test_blockchain.add_new_transaction(item)
  test_blockchain.mine()
list_ = LinkedList(test_blockchain.chain)

node = list_.head
while node:
  block = node.value
  print('Index = ',block.index)
  print('Data = ',block.transactions)
  print('Timestamp =',block.timestamp)
  print('Previous-Hash =',block.previous_hash)
  print('Current-Hash',block.hash)
  print('Nonce',block.nonce)
  print('------------------------------------------------------------------------------------------------------------')
  node  = node.next

