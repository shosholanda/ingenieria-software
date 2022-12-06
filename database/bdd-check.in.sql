-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: check.in
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

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
-- Table structure for table `actividad`
--

DROP TABLE IF EXISTS `actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividad` (
  `idactividad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text NOT NULL,
  PRIMARY KEY (`idactividad`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividad`
--

LOCK TABLES `actividad` WRITE;
/*!40000 ALTER TABLE `actividad` DISABLE KEYS */;
INSERT INTO `actividad` VALUES (5,'UNO','Juego en grupo de 4 a 8 participantes siguiendo las cartas de UNO y sus reglas'),(6,'ONO','Juego en grupo de hasta 6 personas donde la suma de las cartas no debe pasar 99'),(7,'JENGA','Juego para empezar a beber');
/*!40000 ALTER TABLE `actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostal`
--

DROP TABLE IF EXISTS `hostal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostal` (
  `idhostal` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `idactividad` int NOT NULL,
  PRIMARY KEY (`idhostal`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostal`
--

LOCK TABLES `hostal` WRITE;
/*!40000 ALTER TABLE `hostal` DISABLE KEYS */;
INSERT INTO `hostal` VALUES (1,'Cajún','Veracruz',5),(2,'Habanero','Guadalajara',7);
/*!40000 ALTER TABLE `hostal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservacion`
--

DROP TABLE IF EXISTS `reservacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservacion` (
  `idreservacion` int NOT NULL AUTO_INCREMENT,
  `correo` varchar(45) DEFAULT NULL,
  `idhostal` int NOT NULL,
  `numero_personas` int NOT NULL,
  `fecha_llegada` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `tipo_reservacion` int NOT NULL,
  PRIMARY KEY (`idreservacion`),
  KEY `Correo_idx` (`correo`),
  KEY `IDHostal_idx` (`idhostal`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservacion`
--

LOCK TABLES `reservacion` WRITE;
/*!40000 ALTER TABLE `reservacion` DISABLE KEYS */;
INSERT INTO `reservacion` VALUES (1,'alberto@check.in.mx',1,5,'2017-06-15','2020-09-10',1),(2,'davidshiro.strom@gmail.com',1,6,'2022-11-28','2022-12-28',1),(3,'davidshiro.strom@gmail.com',1,4,'2022-11-28','2022-12-28',1),(4,'davidshiro.strom@gmail.com',1,4,'2022-11-28','2022-12-28',1),(5,'davidshiro.strom@gmail.com',1,2,'2022-11-28','2022-12-28',1),(6,'alberto@check.in.mx',1,22,'2022-11-27','2022-12-04',1),(7,'davidshiro.strom@gmail.com',1,19,'2022-12-20','2022-12-28',1);
/*!40000 ALTER TABLE `reservacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `correo` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `edad` int NOT NULL,
  `hash_contraseña` varchar(64) NOT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `nacionalidad` varchar(45) NOT NULL,
  `tipo_usuario` int NOT NULL,
  `idactividad` int NOT NULL,
  PRIMARY KEY (`correo`),
  KEY `IDActividad_idx` (`idactividad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('admin@check.in.mx','Admin',0,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9','5555555555','Mundo',0,5),('alberto@check.in.mx','Alberto Reyes',23,'4bdbc215d8dc3c571e802a69bced0c3071cc4a1f129ad97e15b357018aac6cd4','77769854','Acapulco',1,7),('davidshiro.strom@gmail.com','David Silva',34,'07d046d5fac12b3f82daf5035b9aae86db5adc8275ebfbf05ec83005a4a8ba3e','12321312','Mexico',1,4),('davidshiro@check.in.mx','David Silva',24,'87babf8d65f512809e52db93bfa6fe0bc65e1a173ff86ce90fb4efc58abae1b7','5547065499','Mexico',1,6);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 15:23:42
-- contraseñas: Admin=0, David Silva=david Alberto Reyes=alberto 
