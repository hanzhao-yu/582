from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

def getTransaction(tx):
    tx = w3.eth.getTransaction(tx)   #YOUR CODE HERE
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def getGasPrice(tx):
    tx = getTransaction(tx)
    gasPrice = tx.gasPrice #YOUR CODE HERE
    return gasPrice

def getGas(tx):
    tx = w3.eth.getTransactionReceipt(tx)
    gas = tx.gasUsed #YOUR CODE HERE
    return gas

def getTransactionCost(tx):
    txCost = getGasPrice(tx) * getGas(tx)
    return txCost

def getBlockCost(blockNum):
    block = w3.eth.getBlock(blockNum)
    blockCost = 0
    for tx in block.transactions:
        blockCost = blockCost + getTransactionCost(tx)
    return blockCost

# Return the hash of the most expensive transaction
def getMostExpensiveTransaction(blockNum):
    block = w3.eth.getBlock(blockNum)
    maxBlockCost = 0
    maxTx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')
    for tx in block.transactions:
        cost = getTransactionCost(tx)
        if cost > maxBlockCost:
            maxBlockCost = cost
            maxTx = tx
    return maxTx


print(" ".join(hex(n) for n in (b'\xca\x8f\x8c1\\\x8blH\xce\xe0gVw\xb7\x86\xd1\xba\xbergs\x82\x9aX\x8e\xfaP\x0bq\xcb\xdbe')))
