# coding=utf-8
import requests
import json
from db.mysql import initDB, save
from common import property
from common import dal


def start(url):
    print "开始爬取以太坊数据"
    if property.get_value("db.init") != 'true':
        initDB()
    syncBlock = property.getInt("point")
    while True:
        blockNum = getBlockNumber(url)
        if syncBlock < blockNum :
            print ("最新区块高度为: %d ,已经处理的区块高度为 %d " % (blockNum, syncBlock))
            for num in range(syncBlock, blockNum):
                analysisContractTransByNumber(url, num, blockNum)
            syncBlock = blockNum


def getBlockNumber(url):
    parms = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": "1"}
    jsonStr = sendPost(url, parms)
    return int(jsonStr.get("result"), 16)


def analysisContractTransByNumber(url, num, blockNum):
    parms = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [hex(num), True], "id": "1"}
    block = sendPost(url, parms)
    transactions = block.get("result").get("transactions")
    print ("处理第 [%d/%d] 个区块 [%d] 笔交易数据" % (num, blockNum, len(transactions)))
    for transaction in transactions:
        args = splitTranInput(transaction.get("input"))
        if args is not None:
            transaction["gas"] = int(transaction.get("gas"), 16)
            transaction["value"] = int(transaction.get("value"), 16)
            transaction["blockNumber"] = int(transaction.get("blockNumber"), 16)
            transaction["transactionIndex"] = int(transaction.get("transactionIndex"), 16)
            transaction["gasPrice"] = int(transaction.get("gasPrice"), 16)
            transaction["input"] = args
            transaction["timestamp"] = int(block.get("result").get("timestamp"), 16)
            if transaction.get("to") is None:
                transaction["status"] = 0
            else:
                transaction["status"] = 1
            count = save(dal.get_value("insert.eth_contract_transaction"), transaction)
            print ("处理第 [%d/%d] 个区块第 [%d] 笔交易结果 ==> %d" % (num, blockNum, transaction.get("transactionIndex"), count))


def analysisTransactionByHash(url, tran_hash):
    parms = {"jsonrpc": "2.0", "method": "eth_getTransactionByHash", "params": [tran_hash], "id": "1"}
    transaction = sendPost(url, parms)
    print (json.dumps(transaction, skipkeys=True, indent=2))


def analysisBlockByNumber(url, num):
    parms = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [hex(num), True], "id": "1"}
    block = sendPost(url, parms)
    print (json.dumps(block, skipkeys=True, indent=2))


def sendPost(url, parms):
    response = requests.post(url=url, json=parms)
    return response.json()


def splitTranInput(input):
    if input is None or len(input) < 10:
        return
    result = None
    parmms = input[10:len(input)]
    if len(parmms) % 64 == 0:
        method = input[0:10]
        result = method
        size = len(parmms) / 64
        for i in range(0, size):
            result += "," + parmms[i * 64:(i + 1) * 64]
    return result


if __name__ == '__main__':
    URL = "http://10.10.144.96:8545"
    hash = "0xfc8fb2a9871ae6f3c77b1952f836a64e6c796fbe9ce987c058d484d8f8dc86bb"
    analysisTransactionByHash(URL, hash)
    # block_num = 251990
    # analysisBlockByNumber(url=URL,num=block_num)
