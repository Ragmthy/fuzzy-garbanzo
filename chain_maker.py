# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:07 2018

@author: ragini.gurumurthy
"""

from blockchain import Block
import datetime

num_blocks_to_add = int(input("Enter the number of blocks to add on: "))

block_chain = [Block.genesis_block()]

print("The genesis block has been created")
print("Hash: {}".format(block_chain[0].hash))

for i in range(1, num_blocks_to_add+1):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Data for the block",
                             datetime.datetime.now()))
    
    print("Block {} created".format(i))
    print("Hash: {}".format(block_chain[-1].hash))