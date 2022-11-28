ALTER TABLE `Ventes` CHANGE `?` `Code_Depot` char(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL;
ALTER TABLE `Ventes` ADD FOREIGN KEY (`Code_Depot`) REFERENCES `Depot` (`Code_Depot`);
