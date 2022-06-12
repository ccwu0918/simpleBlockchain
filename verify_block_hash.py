#coding:utf-8
import time 
import random
import hashlib
import threading
import MerkleTrees
ground_truth_Tree = MerkleTrees.Jae_MerkTree()
blocks = [block1, block2]

# verifyBlock&txs
for block in blocks:
  
  txHashList = []
  for i in range(len(block["txs"])):
    txHashList.append(block["txs"][i]["txhash"])
  
  print(txHashList)

  ground_truth_transaction = txHashList
  ground_truth_Tree.listoftransaction = ground_truth_transaction
  ground_truth_Tree.create_tree()
  ground_truth_past_transaction = ground_truth_Tree.Get_past_transacion()
  ground_truth_root = ground_truth_Tree.Get_Root_leaf()
  verify_merkleRoot = ground_truth_root

  hashTarget = str(block["previoushash"]) + str(block["unixtime"]) + str (block["difficulty"]) + str(block["version"]) + str(block["merkleRoot"])
  verify_blockhash = hashlib.sha256((hashTarget * block["nonce"]).encode("utf-8")).hexdigest()
  if verify_blockhash == block["blockhash"] and verify_merkleRoot == block["merkleRoot"]:
    print("ok!")
  else:
    print("fail!")
