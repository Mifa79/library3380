-- MySQL dump 10.13  Distrib 8.0.19, for osx10.15 (x86_64)
--
-- Host: localhost    Database: database_project
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add user',1,'add_user'),(2,'Can change user',1,'change_user'),(3,'Can delete user',1,'delete_user'),(4,'Can view user',1,'view_user'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `ISBN` varchar(50) NOT NULL,
  `book_title` varchar(50) DEFAULT NULL,
  `book_author` varchar(50) DEFAULT NULL,
  `book_publisher` varchar(50) DEFAULT NULL,
  `book_subject` varchar(50) DEFAULT NULL,
  `date_of_publication` date DEFAULT NULL,
  `MSRP` double DEFAULT NULL,
  `total_copy_num` int DEFAULT NULL,
  PRIMARY KEY (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('0544824385','The Way Things Work Now','David Macaulay ','HMH Books for Young Readers','Engineering','2016-06-06',23.65,6),('0615991424','Have Fun with Water Color','Catherine V Holmes','Library Tales Publishing','Art','2014-03-07',14.39,1),('1250301696','The Silent Patient','Alex Michaelides','Celadon Books','Science Fiction','2019-02-05',16.19,2),('1250313074','Ninth House','Alex Stern','Flatiron Books','Science Fiction','2019-10-08',16.78,1),('1465473637','Science for All','DK','DK Children','Science','2018-07-08',20.99,1),('1524759783','Recursion: A Novel','Blake Crouch','Crown','Science Fiction','2019-06-11',17.06,1),('70778709','Beautiful Color Palettes','Catherine V Holmes','Lake Union Publishing','Art','2016-06-06',26.12,1),('87987968','The Art of Typography','Alex Stern','Library Tales Publishing','Art','2019-06-11',30.65,1),('B0192CTMYG','Harry Potter - Part 1','J.K. Rowling','Pottermore Publishing','Science Fiction','2015-12-08',6.89,1),('BO7GVK5HW8','The Overdue Life of Amy','Kelly Harms','Lake Union Publishing','Science Fiction','2019-05-01',5.99,1),('BO7NVD1276','In An Instant','Suzanne Redfearn','Lake Union Publishing','Science Fiction','2020-03-01',12.99,2),('EH898HOI','College Algebra','David Macaulay ','HMH','Math','2016-06-06',14.98,1),('JLII80970','Introduction to Statistic','Kelly Harms','Crown','Math','2020-03-01',12.88,1);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `copy`
--

DROP TABLE IF EXISTS `copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `copy` (
  `copy_ID` int NOT NULL AUTO_INCREMENT,
  `item_ID` varchar(50) NOT NULL,
  `loaned` tinyint(1) NOT NULL,
  `damaged` tinyint(1) NOT NULL,
  `lost` tinyint(1) NOT NULL,
  `item_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`copy_ID`,`item_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copy`
--

LOCK TABLES `copy` WRITE;
/*!40000 ALTER TABLE `copy` DISABLE KEYS */;
INSERT INTO `copy` VALUES (1,'0544824385',0,0,0,'book'),(2,'0544824385',0,0,0,'book'),(3,'0544824385',0,0,0,'book'),(4,'0544824385',0,0,0,'book'),(5,'0544824385',0,0,0,'book'),(6,'AIRij879',0,0,0,'laptop'),(7,'AIRij879',0,0,0,'laptop'),(8,'MAC3463',0,0,0,'laptop'),(9,'MAC3463',0,0,0,'laptop'),(10,'VIVO223',0,0,0,'laptop'),(11,'VIVO223',0,0,0,'laptop'),(12,'457457',1,0,0,'media'),(13,'457457',0,0,0,'media'),(14,'90970',0,0,0,'media'),(15,'90970',0,0,0,'media'),(16,'1250301696',0,0,0,'book'),(17,'1250301696',0,0,0,'book'),(18,'1250313074',0,0,0,'book'),(19,'0615991424',0,0,0,'book'),(20,'1524759783',0,0,0,'book'),(21,'70778709',0,0,0,'book'),(22,'87987968',0,0,0,'book'),(23,'BO7NVD1276',0,0,0,'book'),(24,'BO7NVD1276',0,0,0,'book'),(25,'EH898HOI',0,0,0,'book'),(26,'JLII80970',0,0,0,'book'),(27,'HP9879',0,0,0,'laptop'),(28,'LENO879',0,0,0,'laptop'),(29,'MAC3463',0,0,0,'laptop'),(30,'1465473637',0,0,0,'book'),(31,'B0192CTMYG',0,0,0,'book'),(32,'BO7GVK5HW8',0,0,0,'book'),(33,'HP9709',0,0,0,'laptop'),(35,'0544824385',0,0,0,'book'),(36,'LENO879',0,0,0,'laptop'),(37,'364577',0,0,0,'media');
/*!40000 ALTER TABLE `copy` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `copy.count_book_copy` AFTER INSERT ON `copy` FOR EACH ROW BEGIN
	IF NEW.item_type = "book" THEN
        UPDATE `database_project`.`book` SET total_copy_num = total_copy_num + 1
        WHERE ISBN = NEW.item_ID;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `copy.count_laptop_copy` AFTER INSERT ON `copy` FOR EACH ROW BEGIN
	IF NEW.item_type = "laptop" THEN
        UPDATE `database_project`.`laptop` SET total_copy_num = total_copy_num + 1
        WHERE lap_model = NEW.item_ID;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `copy.count_media_copy` AFTER INSERT ON `copy` FOR EACH ROW BEGIN
	IF NEW.item_type = "media" THEN
        UPDATE `database_project`.`media` SET total_copy_num = total_copy_num + 1
        WHERE media_ID = NEW.item_ID;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_sign_up_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_sign_up_user_id` FOREIGN KEY (`user_id`) REFERENCES `sign_up_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(1,'sign_up','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-06 01:10:55.060732'),(2,'contenttypes','0002_remove_content_type_name','2020-04-06 01:10:55.124022'),(3,'auth','0001_initial','2020-04-06 01:10:55.156907'),(4,'auth','0002_alter_permission_name_max_length','2020-04-06 01:10:55.241922'),(5,'auth','0003_alter_user_email_max_length','2020-04-06 01:10:55.247109'),(6,'auth','0004_alter_user_username_opts','2020-04-06 01:10:55.251994'),(7,'auth','0005_alter_user_last_login_null','2020-04-06 01:10:55.257806'),(8,'auth','0006_require_contenttypes_0002','2020-04-06 01:10:55.260120'),(9,'auth','0007_alter_validators_add_error_messages','2020-04-06 01:10:55.265215'),(10,'auth','0008_alter_user_username_max_length','2020-04-06 01:10:55.270994'),(11,'auth','0009_alter_user_last_name_max_length','2020-04-06 01:10:55.276389'),(12,'auth','0010_alter_group_name_max_length','2020-04-06 01:10:55.299028'),(13,'auth','0011_update_proxy_permissions','2020-04-06 01:10:55.304977'),(14,'sign_up','0001_initial','2020-04-06 01:10:55.358135'),(15,'admin','0001_initial','2020-04-06 01:10:55.440874'),(16,'admin','0002_logentry_remove_auto_add','2020-04-06 01:10:55.484022'),(17,'admin','0003_logentry_add_action_flag_choices','2020-04-06 01:10:55.491320'),(18,'sessions','0001_initial','2020-04-06 01:10:55.515461');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('wz7w0kxng4c82of4fnx3xzd9dfvdaxzu','NzY2MDQzY2NlMzI0YTZlMjhjNDA0OTI1OWM2OTViNDQxOTY3OTViYzp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImxpYnJhcnkzMzgwLmF1dGhlbnRpY2F0aW9uLlNldHRpbmdzQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjM3ZDMzMmY4NjY3YTJkZjZjMjYwM2JlMGUzMjY2NWQ3ZDU1YWJkNTcifQ==','2020-04-30 22:33:23.153464');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fine`
--

DROP TABLE IF EXISTS `fine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fine` (
  `fine_ID` int NOT NULL AUTO_INCREMENT,
  `loan_ID` int NOT NULL,
  `user_ID` int NOT NULL,
  `amount_due` double NOT NULL DEFAULT '0',
  `paid` tinyint(1) NOT NULL,
  PRIMARY KEY (`fine_ID`),
  KEY `FK_sign_up_user_0_fine_idx` (`user_ID`),
  CONSTRAINT `FK_sign_up_user_0_fine` FOREIGN KEY (`user_ID`) REFERENCES `sign_up_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fine`
--

LOCK TABLES `fine` WRITE;
/*!40000 ALTER TABLE `fine` DISABLE KEYS */;
INSERT INTO `fine` VALUES (42,67,18,820,0),(43,66,18,11.825,0);
/*!40000 ALTER TABLE `fine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laptop`
--

DROP TABLE IF EXISTS `laptop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laptop` (
  `lap_model` varchar(50) NOT NULL,
  `lap_OS` varchar(50) DEFAULT NULL,
  `date_of_manufacture` date DEFAULT NULL,
  `MSRP` double DEFAULT NULL COMMENT 'MSRP IN DOLLARS',
  `lap_manufacturer` varchar(50) DEFAULT NULL,
  `total_copy_num` int DEFAULT NULL,
  PRIMARY KEY (`lap_model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laptop`
--

LOCK TABLES `laptop` WRITE;
/*!40000 ALTER TABLE `laptop` DISABLE KEYS */;
INSERT INTO `laptop` VALUES ('AIRij879','Mac','2018-06-05',800,'Apple',2),('HP9709','Window','2018-06-05',360,'HP',1),('HP9879','Window','2018-06-05',700,'HP',1),('LENO879','Window','2018-06-05',820,'Lenovo',2),('MAC3463','Mac','2018-06-05',1200,'Apple',3),('VIVO223','Window','2018-06-05',750,'Samsung',2);
/*!40000 ALTER TABLE `laptop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `loan_ID` int NOT NULL AUTO_INCREMENT,
  `user_ID` int NOT NULL,
  `user_type_ID` varchar(5) DEFAULT NULL,
  `item_ID` varchar(50) NOT NULL,
  `item_copy_ID` int NOT NULL,
  `item_type` varchar(10) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `return_due_date` date DEFAULT NULL,
  `overdue_date_num` int DEFAULT NULL,
  `damaged` tinyint(1) DEFAULT NULL,
  `lost` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`loan_ID`),
  KEY `FK_copy_0_loan_idx` (`item_copy_ID`),
  KEY `FK_sign_up_user_0_loan_idx` (`user_ID`),
  CONSTRAINT `FK_sign_up_user_0_loan` FOREIGN KEY (`user_ID`) REFERENCES `sign_up_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (66,18,'1','0544824385',1,'book','2020-04-16','2020-05-16',0,1,0,0),(67,18,'1','LENO879',28,'laptop','2020-04-16','2020-05-16',0,0,1,0),(68,18,'1','457457',12,'media','2020-04-16','2020-05-16',NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.late_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.overdue_date_num > 0 THEN

        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, NEW.overdue_date_num * (SELECT overdue_fine_rate FROM `database_project`.`user_type_info` WHERE user_type_ID = old.user_type_ID));
        
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.book_damaged_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.damaged = 1 and old.item_type = "book"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, 0.5 * (SELECT MSRP FROM `database_project`.`book` WHERE ISBN = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.book_lost_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.lost = 1 and old.item_type = "book"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, (SELECT MSRP FROM `database_project`.`book` WHERE ISBN = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.laptop_lost_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.lost = 1 and old.item_type = "laptop"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, (SELECT MSRP FROM `database_project`.`laptop` WHERE lap_model = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.laptop_damaged_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.damaged = 1 and old.item_type = "laptop"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, 0.6 * (SELECT MSRP FROM `database_project`.`laptop` WHERE lap_model = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.media_damaged_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.damaged = 1 and old.item_type = "media"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, 0.6 * (SELECT MSRP FROM `database_project`.`media` WHERE media_ID = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `loan.media_lost_fine` AFTER UPDATE ON `loan` FOR EACH ROW BEGIN
	IF NEW.lost = 1 and old.item_type = "media"  THEN
        INSERT INTO `database_project`.`fine`(loan_ID, user_ID, paid, amount_due)
        VALUES (old.loan_ID, old.user_ID, 0, (SELECT MSRP FROM `database_project`.`media` WHERE media_ID = old.item_ID));
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `media` (
  `media_ID` varchar(50) NOT NULL,
  `media_title` varchar(50) DEFAULT NULL,
  `media_author` varchar(30) DEFAULT NULL,
  `media_publisher` varchar(60) DEFAULT NULL,
  `media_subject` varchar(25) DEFAULT NULL,
  `media_date_publication` date DEFAULT NULL,
  `MSRP` double DEFAULT NULL COMMENT 'MSRP IN DOLLARS',
  `total_copy_num` int DEFAULT NULL,
  PRIMARY KEY (`media_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media`
--

LOCK TABLES `media` WRITE;
/*!40000 ALTER TABLE `media` DISABLE KEYS */;
INSERT INTO `media` VALUES ('364577','Sacrify','Elton John','Elton John','Music','2017-06-08',16.69,1),('457457','The Circle of Life','Anthony Michael Hall','MAC3463','Science','2018-07-06',12.54,2),('46477','Alaska Wildlife','Sandy Hugman','The Rainforest','Wildlife','2018-07-06',15.45,0),('869686','Spirit of Time','Esta Tonne','Esta Tonne','Music','2019-07-06',12.96,0),('90970','American History','Richard Kurin','The Great Courses','History','2017-06-08',14.69,2),('9868756','Don\'t Know Why','Norah Jones','The Hall','Music','2018-07-06',20.34,0);
/*!40000 ALTER TABLE `media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserve`
--

DROP TABLE IF EXISTS `reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserve` (
  `reservation_ID` int NOT NULL AUTO_INCREMENT,
  `reservation_date` date NOT NULL,
  `user_ID` int NOT NULL,
  `item_ID` varchar(50) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`reservation_ID`),
  KEY `FK_book_0_reserve_idx` (`item_ID`),
  KEY `FK_sign_up_user_0_reserve_idx` (`user_ID`),
  CONSTRAINT `FK_book_0_reserve` FOREIGN KEY (`item_ID`) REFERENCES `book` (`ISBN`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_laptop_0_reserve` FOREIGN KEY (`item_ID`) REFERENCES `laptop` (`lap_model`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_media_0_reseve` FOREIGN KEY (`item_ID`) REFERENCES `media` (`media_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_sign_up_user_0_reserve` FOREIGN KEY (`user_ID`) REFERENCES `sign_up_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserve`
--

LOCK TABLES `reserve` WRITE;
/*!40000 ALTER TABLE `reserve` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserve` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_up_user`
--

DROP TABLE IF EXISTS `sign_up_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_up_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_user_type_info_0_sign_up_user_idx` (`user_type`),
  CONSTRAINT `fk_user_type_info_0_sign_up_user` FOREIGN KEY (`user_type`) REFERENCES `user_type_info` (`user_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_up_user`
--

LOCK TABLES `sign_up_user` WRITE;
/*!40000 ALTER TABLE `sign_up_user` DISABLE KEYS */;
INSERT INTO `sign_up_user` VALUES (18,'pbkdf2_sha256$180000$2cRo7MDbOpbZ$ZrDOGdoMVHuhJRA1JNVN7WEE4qfnGqx3JCQu/yBYS4M=','2020-04-16 22:33:23.151771',0,'stud1','John','Doe','stud1@gmail.com',0,1,'2020-04-16 22:31:44.561677','1');
/*!40000 ALTER TABLE `sign_up_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_up_user_groups`
--

DROP TABLE IF EXISTS `sign_up_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_up_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sign_up_user_groups_user_id_group_id_7a5daa55_uniq` (`user_id`,`group_id`),
  KEY `sign_up_user_groups_group_id_ab77d190_fk_auth_group_id` (`group_id`),
  CONSTRAINT `sign_up_user_groups_group_id_ab77d190_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `sign_up_user_groups_user_id_3ac0ad00_fk_sign_up_user_id` FOREIGN KEY (`user_id`) REFERENCES `sign_up_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_up_user_groups`
--

LOCK TABLES `sign_up_user_groups` WRITE;
/*!40000 ALTER TABLE `sign_up_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `sign_up_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_up_user_user_permissions`
--

DROP TABLE IF EXISTS `sign_up_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_up_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sign_up_user_user_permis_user_id_permission_id_2cce9fc4_uniq` (`user_id`,`permission_id`),
  KEY `sign_up_user_user_pe_permission_id_3593c270_fk_auth_perm` (`permission_id`),
  CONSTRAINT `sign_up_user_user_pe_permission_id_3593c270_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `sign_up_user_user_pe_user_id_97c1dd0e_fk_sign_up_u` FOREIGN KEY (`user_id`) REFERENCES `sign_up_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_up_user_user_permissions`
--

LOCK TABLES `sign_up_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `sign_up_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `sign_up_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_type_info`
--

DROP TABLE IF EXISTS `user_type_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_type_info` (
  `user_type_id` varchar(5) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `user_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `borrow_time_limit` int DEFAULT NULL,
  `borrow_amount_limit` int DEFAULT NULL,
  `reservation_amount_limit` int DEFAULT NULL,
  `overdue_fine_rate` double DEFAULT NULL,
  PRIMARY KEY (`user_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_type_info`
--

LOCK TABLES `user_type_info` WRITE;
/*!40000 ALTER TABLE `user_type_info` DISABLE KEYS */;
INSERT INTO `user_type_info` VALUES ('1','student',30,3,3,0.5),('2','faculty',60,4,5,0.6),('3','employee',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_type_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-20 16:01:58
