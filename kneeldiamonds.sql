CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NUMERIC(3,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO `Styles` VALUES (null, "Classic", 500.00);
INSERT INTO `Styles` VALUES (null, "Modern", 710.00);
INSERT INTO `Styles` VALUES (null, "Vintage", 965.00);

INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.40);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.90);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241.00);

INSERT INTO `Sizes` VALUES (null, 0.5, 405.00);
INSERT INTO `Sizes` VALUES (null, 0.75, 782.00);
INSERT INTO `Sizes` VALUES (null, 1.00, 1470.00);
INSERT INTO `Sizes` VALUES (null, 1.50, 1997.00);
INSERT INTO `Sizes` VALUES (null, 2.00, 3638.00);

INSERT INTO `Orders` VALUES (null, 1, 2, 3, CURRENT_TIMESTAMP);
INSERT INTO `Orders` VALUES (null, 3, 5, 2, CURRENT_TIMESTAMP);
INSERT INTO `Orders` VALUES (null, 2, 3, 1, CURRENT_TIMESTAMP);
INSERT INTO `Orders` VALUES (null, 3, 4, 3, CURRENT_TIMESTAMP);
INSERT INTO `Orders` VALUES (null, 4, 4, 3, CURRENT_TIMESTAMP);
INSERT INTO `Orders` VALUES (null, 5, 5, 2, CURRENT_TIMESTAMP);

ALTER TABLE `Orders` DROP `timestamp`;
ALTER TABLE `Orders` ADD `timestamp` CURRENT_TIMESTAMP;

