-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recetas_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recetas_db` ;

-- -----------------------------------------------------
-- Schema recetas_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recetas_db` DEFAULT CHARACTER SET utf8 ;
USE `recetas_db` ;

-- -----------------------------------------------------
-- Table `recetas_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recetas_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recetas_db`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recetas_db`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` TEXT NOT NULL,
  `instruction` TEXT NOT NULL,
  `date_on` DATE NOT NULL,
  `under` VARCHAR(3) NOT NULL,
  `key_likes` INT NOT NULL,
  `likes` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_TV_shows_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_TV_shows_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `recetas_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;