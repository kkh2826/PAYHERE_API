CREATE TABLE `userinfo` (
  `email` varchar(50) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
