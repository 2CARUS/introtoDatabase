CREATE DATABASE  IF NOT EXISTS `not_the_home_depot`;
USE `not_the_home_depot`;

SET NAMES utf8 ;

DROP TABLE IF EXISTS `supplier`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `supplier` (
  `supplier_id` INT(9) NOT NULL,
  `sup_name` VARCHAR(20) NOT NULL,
  `sup_phone` INT(10) NOT NULL,
  `sup_details` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`sup_id`)
);



DROP TABLE IF EXISTS `supplier_address`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `supplier_address` (
  `supp_id` INT(9) NOT NULL,
  `supp_addr_id` INT(9) NOT NULL,
  `date_from` DATETIME DEFAULT NULL,
  `date_to` DATETIME DEFAULT NULL,
  PRIMARY KEY (`supp_addr_id`, `supp_id`),
  FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`supplier_id`),
  FOREIGN KEY (`supp_addr_id`) REFERENCES `address` (`address_id`)
);



DROP TABLE IF EXISTS `address`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `address` (
  `address_id` INT(9) NOT NULL,
  `country` VARCHAR(30) NOT NULL,
  `state` VARCHAR(30) NOT NULL,
  `city` VARCHAR(30) NOT NULL,
  `street` VARCHAR(30) NOT NULL,
  `building_number` INT(9) NOT NULL,
  `apartment` INT(3),
  `zip` INT(5) NOT NULL,
  PRIMARY KEY (`address_id`)
);



DROP TABLE IF EXISTS `product_supplier`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `product_supplier` (
  `prod_id` INT(9) NOT NULL,
  `supp_id` INT(9) NOT NULL,
  `date_supplied_from` DATETIME DEFAULT NULL,
  `date_supplied_to` DATETIME DEFAULT NULL,
  `amount_purchased` INT(5) DEFAULT NULL,
  `value_purchased` DECIMAL(13,2) DEFAULT NULL,
  PRIMARY KEY (`prod_id`, `supp_id`),
  FOREIGN KEY (`prod_id`) REFERENCES `product` (`product_id`),
  FOREIGN KEY (`supp_id`) REFERENCES `supplier` (`supplier_id`)
);



DROP TABLE IF EXISTS `customer`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `customer_id` INT(9) NOT NULL,
  `customer_name` VARCHAR(50) NOT NULL,
  `cutomer_phone` INT(10) NOT NULL,
  `customer_email` VARCHAR(30) NOT NULL,
  `customer_addr_id` INT(9) NOT NULL,
  `pay_me_id` INT(9) NOT NULL,
  PRIMARY KEY (`customer_id`),
  FOREIGN KEY (`customer_addr_id`) REFERENCES `customer_address` (`cust_addr_id`),
  FOREIGN KEY (`pay_me_id`) REFERENCES `payment_method` (`payment_method_id`)
);



DROP TABLE IF EXISTS `customer_address`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `customer_address` (
  `cust_addr_id` INT(9) NOT NULL,
  `addr_id` INT(9) NOT NULL,
  PRIMARY KEY (`cust_id`,`addr_id`),
  FOREIGN KEY (`cust_id`) REFERENCES `customer` (`customer_id`),
  FOREIGN KEY (`addr_id`) REFERENCES `address` (`address_id`)
);



DROP TABLE IF EXISTS `department_store`;
SET character_set_client = utf8mb4;
CREATE TABLE `department_store` (
  `store_id` INT(9) NOT NULL,
  `store_name` VARCHAR(30) NOT NULL,
  `store_addr_id` INT(9) NOT NULL,
  `store_phone` INT(10) NOT NULL,
  `store_email` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`store_id`),
  FOREIGN KEY (`store_addr_id`) REFERENCES `address` (`adress_id`),
);



DROP TABLE IF EXISTS `store_address`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `store_address` (
  `st_addr_id` INT(9) NOT NULL,
  `addr_id` INT(9) NOT NULL,
  PRIMARY KEY (`st_addr_id`,`addr_id`),
  FOREIGN KEY (`st_addr_id`) REFERENCES `department_store` (`store_addr_id`),
  FOREIGN KEY (`addr_id`) REFERENCES `address` (`address_id`)
);



DROP TABLE IF EXISTS `payment_method`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `customer_address` (
  `payment_method_id` INT(9) NOT NULL,
  `method_type` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`payment_method_id`)
);



DROP TABLE IF EXISTS `department`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `department` (
  `department_id` INT(9) NOT NULL,
  `store_id` INT(9) NOT NULL,
  `department_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`department_id`),
  FOREIGN KEY (`store_id`) REFERENCES `department_store` (`store_id`)
);



DROP TABLE IF EXISTS `product`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `product` (
  `product_id` INT(9) NOT NULL,
  `product_name` VARCHAR(20) NOT NULL,
  `product_price` DECIMAL(13,2) NOT NULL,
  `product_description` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
);



DROP TABLE IF EXISTS `customer_order`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `customer_order` (
  `order_id` INT(9) NOT NULL,
  `cust_id` INT(9) NOT NULL,
  `order_status_id` INT(9) NOT NULL,
  `order_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  FOREIGN KEY `cust_id` REFERENCES `customer` (`customer_id`),
  FOREIGN KEY `order_status_id` REFERENCES `order_status_code` (`status_code`)
);



DROP TABLE IF EXISTS `order_status_code`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `order_status_code` (
  `order_status_description` VARCHAR(40) NOT NULL,
  `status_code` INT(9) NOT NULL,
  PRIMARY KEY (`status_code`)
);



DROP TABLE IF EXISTS `order_item`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `order_item` (
  `order_item_id` INT(9) NOT NULL,
  `ord_id` INT(9) NOT NULL,
  `prod_id` INT(9) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  FOREIGN KEY `ord_id` REFERENCES `customer_order` (`order_id`),
  FOREIGN KEY `prod_id` REFERENCES `product` (`product_id`)
);



DROP TABLE IF EXISTS `staff`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `staff` (
  `staff_id` INT(9) NOT NULL,
  `staff_gender` VARCHAR(10) NOT NULL,
  `staff_name` INT(9) NOT NULL,
  `staff_details` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
);



DROP TABLE IF EXISTS `staff_allocation`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `staff_allocation` (
  `sta_id` INT(9) NOT NULL,
  `dept_id` INT(9) NOT NULL,
  PRIMARY KEY (`sta_id`, `dept_id`),
  FOREIGN KEY `sta_id` REFERENCES `staff` (`staff_id`),
  FOREIGN KEY `dept_id` REFERENCES `department` (`department_id`)
);