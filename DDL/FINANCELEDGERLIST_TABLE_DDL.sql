CREATE TABLE `financeledgerlist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `stdDate` date NOT NULL,
  `email` varchar(50) NOT NULL,
  `seq` int(11) NOT NULL,
  `amount` bigint(20) NOT NULL,
  `payType` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `financeledgerlist_stdDate_email_seq_ecf32646_uniq` (`stdDate`,`email`,`seq`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
