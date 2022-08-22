DROP DATABASE IF EXISTS Statistics;
CREATE DATABASE Statistics;


-- -----------------------------------------------------
-- Table `Statistics`.`CPU` 
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Statistics`.`CPU` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`CPU` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `Utilization` VARCHAR(255),
 `time` TIME,
 PRIMARY KEY (`Id`));

-- -----------------------------------------------------
-- Table `Statistics`.`CPUNow` 
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Statistics`.`CPUNow` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`CPUNow` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `Utilization` VARCHAR(255),
 `time` TIME,
 PRIMARY KEY (`Id`));

-- -----------------------------------------------------
-- Table `Statistics`.`Disk` 
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Statistics`.`Disk` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`Disk` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `used` VARCHAR(255),
 `total` VARCHAR(255),
 `free` VARCHAR(255),
 `time` TIME,
  PRIMARY KEY (`id`));

-- -----------------------------------------------------
-- Table `Statistics`.`DiskNow` 
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Statistics`.`DiskNow` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`DiskNow` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `used` VARCHAR(255),
 `total` VARCHAR(255),
 `free` VARCHAR(255),
 `time` TIME,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `Statistics`.`Memory` 
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Statistics`.`Memory` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`Memory` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `used` VARCHAR(255),
 `total` VARCHAR(255),
 `free` VARCHAR(255),
 `time` TIME,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `Statistics`.`MemoryNow` 
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Statistics`.`MemoryNow` ;

CREATE TABLE IF NOT EXISTS `Statistics`.`MemoryNow` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `used` VARCHAR(255),
 `total` VARCHAR(255),
 `free` VARCHAR(255),
 `time` TIME,
  PRIMARY KEY (`id`));

