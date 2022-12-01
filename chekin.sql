-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema check.in
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema check.in
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `check.in` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `check.in` ;

-- -----------------------------------------------------
-- Table `check.in`.`Actividad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `check.in`.`Actividad` (
  `IDActividad` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(50) NOT NULL,
  `Descripcion` TEXT(100) NOT NULL,
  PRIMARY KEY (`IDActividad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `check.in`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `check.in`.`Usuario` (
  `Correo` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Edad` INT NOT NULL,
  `HashContrasenia` VARCHAR(64) NOT NULL,
  `Celular` VARCHAR(10) NULL,
  `Nacionalidad` VARCHAR(45) NOT NULL,
  `TipoDeUsuario` INT NOT NULL,
  `IDActividad` INT NOT NULL,
  PRIMARY KEY (`Correo`),
  INDEX `IDActividad_idx` (`IDActividad` ASC) VISIBLE,
  CONSTRAINT `IDActividad`
    FOREIGN KEY (`IDActividad`)
    REFERENCES `check.in`.`Actividad` (`IDActividad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `check.in`.`Hostal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `check.in`.`Hostal` (
  `IDHostal` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Estado` INT NOT NULL,
  `IDActividad` INT NOT NULL,
  PRIMARY KEY (`IDHostal`),
  INDEX `IDActividad_idx` (`IDActividad` ASC) VISIBLE,
  CONSTRAINT `IDActividad`
    FOREIGN KEY (`IDActividad`)
    REFERENCES `check.in`.`Actividad` (`IDActividad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `check.in`.`Reservacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `check.in`.`Reservacion` (
  `idReservacion` INT NOT NULL AUTO_INCREMENT,
  `Correo` VARCHAR(45) NULL,
  `IDHostal` INT NOT NULL,
  `NumeroPersonas` INT NOT NULL,
  `FechaLlegada` DATE NOT NULL,
  `FechaSalida` DATE NOT NULL,
  `TipoReservacion` INT NOT NULL,
  PRIMARY KEY (`idReservacion`),
  INDEX `Correo_idx` (`Correo` ASC) VISIBLE,
  INDEX `IDHostal_idx` (`IDHostal` ASC) VISIBLE,
  CONSTRAINT `Correo`
    FOREIGN KEY (`Correo`)
    REFERENCES `check.in`.`Usuario` (`Correo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `IDHostal`
    FOREIGN KEY (`IDHostal`)
    REFERENCES `check.in`.`Hostal` (`IDHostal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;