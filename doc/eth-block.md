以太坊快结构解析：

    RPC 接口： {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [blocknum, True], "id": "1"}

    {
      "jsonrpc": "2.0", 
      "id": "1", 
      "result": {
        "nonce": "0x6dd38dad5ee2fbc2", 
        "receiptsRoot": "0xa220d9c561a474744fa7e3b50a1b26998414ca4a263af3c989321dea1dfdc997", 
        "hash": "0x89e164ea15c475635c32061db704e41e012d7328d0adcd5f84315e9c29a5f453", 
        "uncles": [], 
        "timestamp": "0x55fbdd91", 
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347", 
        "miner": "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5", 
        "parentHash": "0x98fdb6763766062cb4b514fa7af09aaa608f1450c69db21928bb991dff53501c", 
        "extraData": "0xd783010103844765746887676f312e342e32856c696e7578", 
        "gasLimit": "0x2ff5c5", 
        "number": "0x3d856", 
        "stateRoot": "0xe02c456b72f2690b7ff3009fe75cb6b422d3994e2341bfcb206ed876a17418e3", 
        "difficulty": "0x5293fef7b7f", 
        "transactionsRoot": "0x9c3caee64fbebd3b6c5f3357af0295879342888bcad46c27d4528fcb849f61d7", 
        "size": "0x36d", 
        "transactions": [
            ......
        ], 
        "mixHash": "0xc3d756f666aa7101e8427623bf8b79f0d82c5cd14e8fd08d2379440366e90889", 
        "totalDifficulty": "0xf0b5f76d4005cd9", 
        "gasUsed": "0xf348", 
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      }
    }

| 字段名 | 含义 | 备注 |
| :-----| ----: | :----: |
| nonce | 随机数 |  |
| receiptsRoot | 表示transaction执行成功失败还有执行顺序 | 存储的是交易回执内容 |
| hash | 区块hash |  |
| uncles | 叔伯区块 |  |
| timestamp | 时间戳 |  |
| sha3Uncles | 叔块集合的哈希值 | 用于校验 |
| miner | 旷工 |  |
| parentHash | 前块hash |  |
| extraData | 备注内容 |  |
| gasLimit | gas上限 |  |
| number | 区块编号  |  |
| stateRoot | 世界状态 | 记录 transaction执行结束之后的世界状态 |
| difficulty | 难度值 |  |
| transactionsRoot | 交易根hash |  |
| size | 区块大小 |  |
| transactions | 交易集合 |  |
| mixHash | 混合哈希 |  |
| totalDifficulty | 总难度 |  |
| gasUsed | gas使用 |  |
| logsBloom | 日志Bloom值 |  |