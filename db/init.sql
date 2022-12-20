CREATE DATABASE  IF NOT EXISTS `db_sample` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_sample`;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `UID` int(11) NOT NULL AUTO_INCREMENT,
  `UNAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `UPASS` varchar(150) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'sheikhoo','sheikhoo.iran@gmail.com','pbkdf2:sha256:260000$GmB5KcnO2hxXObef$e6ac77013d65ca38f2765209b8b21687c0b51f7572b53ed1e578699240720aee');
UNLOCK TABLES;

