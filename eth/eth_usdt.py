# coding=utf-8
import requests
import json
from db.mysql import initDB, save
from common import property
from common import dal


def start(url):
    print "开始爬取以太坊 USDT 数据"
    if property.get_value("db.init") != 'true':
        initDB()
    syncBlock = property.getInt("point")
    while True:
        blockNum = getBlockNumber(url)
        if syncBlock < blockNum :
            print ("最新区块高度为: %d ,已经处理的区块高度为 %d " % (blockNum, syncBlock))
            for num in range(syncBlock, blockNum):
                analysisUSDTTransByNumber(url, num, blockNum, trans={})
            syncBlock = blockNum


def getBlockNumber(url):
    parms = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": "1"}
    jsonStr = sendPost(url, parms)
    return int(jsonStr.get("result"), 16)


def analysisUSDTTransByNumber(url, num, blockNum, trans):
    parms = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [hex(num), True], "id": "1"}
    block = sendPost(url, parms)
    transactions = block.get("result").get("transactions")
    usdt_count = 0
    for transaction in transactions:
        toAddress = transaction.get("to")
        if toAddress == "0xdac17f958d2ee523a2206206994597c13d831ec7":
            trans["txid"] = transaction.get("hash")
            trans["blockNumber"] = int(transaction.get("blockNumber"), 16)
            trans["from"] = transaction.get("from")
            trans["timestamp"] = int(block.get("result").get("timestamp"), 16)
            trans["type"] = 1
            trans = splitTranInput(transaction.get("input"), trans)
            save(dal.get_value("insert.eth_USDT_transaction"), trans)
            usdt_count = usdt_count + 1
    print ("blocknum=%d    trans=%d   USDT=%d" % (num, len(transactions), usdt_count))


def sendPost(url, parms):
    response = requests.post(url=url, json=parms)
    return response.json()


def splitTranInput(input, trans):
    if input is None or len(input) < 10:
        return
    parmms = input[10:len(input)]
    if len(parmms) % 64 == 0:
        method = input[0:10]
        trans["method"] = method
        _to = parmms[0:64]
        trans["to"] = "0x" + _to[len(_to)-40:len(_to)]
        trans["amount"] = int(parmms[64:128], 16)
    return trans
