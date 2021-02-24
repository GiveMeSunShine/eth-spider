CREATE TABLE `eth_contract_transaction` (
  `hash` char(66) NOT NULL COMMENT 'transaction hash',
  `block_number` bigint(16) unsigned NOT NULL COMMENT 'block number',
  `transaction_index` int(8) unsigned NOT NULL DEFAULT 0 COMMENT 'transaction position index',
  `from` char(42) NOT NULL COMMENT 'he sender account address',
  `to` char(42) COMMENT 'the receiver account address',
  `value` decimal(32,0) DEFAULT NULL COMMENT 'value of transaction in Gwei',
  `gas` int(8) DEFAULT NULL COMMENT 'gas',
  `gas_price` bigint(16) DEFAULT NULL COMMENT 'gas price',
  `status` tinyint(2) NOT NULL DEFAULT 1 COMMENT 'transaction status, 0: failed; 1: success; ',
  `timestamp` bigint(20) DEFAULT NULL COMMENT 'transaction timestamp',
  `parms` LONGTEXT DEFAULT NULL COMMENT 'transaction contract parms',
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`hash`),
  KEY `idx_transaction_from` (`from`),
  KEY `idx_transaction_to` (`to`),
  KEY `idx_blknumber_txindex` (`block_number`,`transaction_index`),
  KEY `idx_transaction_timestamp` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE `usdt` (
  `blocknum` bigint(20) DEFAULT NULL COMMENT '所属区块号',
  `txid` varchar(66) NOT NULL COMMENT '交易ID',
  `from` varchar(66) DEFAULT NULL,
  `to` varchar(66) DEFAULT NULL,
  `amount` decimal(32,8) DEFAULT NULL COMMENT '金额',
  `type` tinyint(4) NOT NULL COMMENT '0:omni、1:ERC20、2:TRC20',
  PRIMARY KEY (`txid`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin