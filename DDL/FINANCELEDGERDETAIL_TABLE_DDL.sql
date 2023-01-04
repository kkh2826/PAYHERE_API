CREATE TABLE `financeledgerdetail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `memo` varchar(1000) DEFAULT NULL,
  `createDate` datetime(6) NOT NULL,
  `updateDate` datetime(6) NOT NULL,
  `financeledger_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `financeledger_id` (`financeledger_id`),
  CONSTRAINT `financeledgerdetail_financeledger_id_145f3cd8_fk_financele` FOREIGN KEY (`financeledger_id`) REFERENCES `financeledgerlist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
