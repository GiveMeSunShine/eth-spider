以太坊交易结构解析：

    RPC 接口： parms = {"jsonrpc": "2.0", "method": "eth_getTransactionByHash", "params": [tran_hash], "id": "1"}
    也可以通过区块获取区块中包含的交易集合进行解析

    {
      "jsonrpc": "2.0", 
      "id": "1", 
      "result": {
        "nonce": "0xc", 
        "hash": "0xb0e580cc2009b265ff3a413ffa47230d23fcbf7f7c2a36f10fd845537b9303f1", 
        "blockHash": "0x32ffea57671a6aa8c7257f671af24ee74ab5671e7e71c93fbd1a1262a4c3f8c1", 
        "v": "0x1b", 
        "gas": "0x15f90", 
        "value": "0x0", 
        "blockNumber": "0x61d7e", 
        "to": null, 
        "s": "0x2b23d01f8388bb57e3a9dcb68e3cb4eb0c8adf79ea099ecbded89b791c486131", 
        "r": "0x71a3d9c5cf7f73dac117ae39c6d7b7790e0cdc2d50a7a225f26cfbfd2d51de8a", 
        "input": "0x609880600c6000396000f30060003560e060020a9004806331e12c2014601f578063d66d6c1014602b57005b6025603d565b60006000f35b6037600435602435605d565b60006000f35b600054600160a060020a0316600014605357605b565b336000819055505b565b600054600160a060020a031633600160a060020a031614607b576094565b8060016000848152602001908152602001600020819055505b505056", 
        "from": "0x8d0b69cc5de9cbb2d565c3ec9ff0cf5adc1a2016", 
        "transactionIndex": "0x0", 
        "gasPrice": "0xba43b7400"
      }
    }

| 字段名 | 含义 | 备注 |
| :-----| ----: | :----: |
| nonce | 随机数 |  |
| hash | 交易hash | |
| blockHash | 所属区块hash |  |
| v | 签名参数 |  |
| gas | gas值 |  |
| value | 转账金额 | 16进制 |
| blockNumber | 区块编号 | 16进制 |
| to | to地址 | 普通账户地址或合约地址 |
| s | 签名参数 |  |
| r | 签名参数 |  |
| input | 备注数据 | 见下文详细秒描述 |
| from | from 地址 |  |
| transactionIndex | 交易序号 | 表示在区块中的编号 |
| gasPrice | gas价格 |  |

>注意：
input 字段根据to地址的不同，内容有所不同，目前已知主要有以下几种：
>
> to 地址为空情况：表示部署合约失败（也有部分是成功，但是to地址未记录，需要通过java 版本代码输出内部交易日志进行补偿）
> 
> to地址不为空，input 数据为 0x，表示该笔交易是普通交易；
> 
> to地址不为空，input 数据页不是0x，则input 数据有三种可能：
> 
> 1.input 长度大于等于10，并且可以截取前十位后，剩下的部分可以按照64位切割成N份(N 可以为0)，同时64位截取中头部都是 0 补位，则表示是合约交易，前10位是 methodID，后 N 个 64 位数据位 方法参数；
> 
> 2.input 长度大于 10，但是没有明显10，64*N 的参数规律，则可能是合约的二进制编码或者是存证数据记录