-- Run this block if you already have a database and need to re-create it
DELETE FROM Metals;
DELETE FROM Sizes;
DELETE FROM Styles;
DELETE FROM Orders

DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Orders;
-- End block

-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Metals` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` FLOAT NOT NULL,
    `price` NUMERIC NOT NULL
);

CREATE TABLE `Styles` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC NOT NULL
);


CREATE TABLE `Orders` (
   `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   `metal_id` INTEGER NOT NULL,
   `size_id` INTEGER NOT NULL,
   `style_id` INTEGER NOT NULL,
   FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
   FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
   FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);



INSERT INTO 'Metals' VALUES (null, "Sterling Silver", 12.42);
INSERT INTO 'Metals' VALUES (null, "14k Gold", 736.4);
INSERT INTO 'Metals' VALUES (null, "24k Gold", 1258.9);
INSERT INTO 'Metals' VALUES (null, "Platinum", 795.45);
INSERT INTO 'Metals' VALUES (null, "Palladium", 1241);

INSERT INTO 'Sizes' VALUES (null, 0.5, 405);
INSERT INTO 'Sizes' VALUES (null, 0.75, 782);
INSERT INTO 'Sizes' VALUES (null, 1, 1470);
INSERT INTO 'Sizes' VALUES (null, 1.5, 1997);
INSERT INTO 'Sizes' VALUES (null, 2, 3638);

INSERT INTO 'Styles' VALUES (null, "Classic", 500);
INSERT INTO 'Styles' VALUES (null, "Modern", 710);
INSERT INTO 'Styles' VALUES (null, "Vintage", 965);

INSERT INTO Orders (metal_id, size_id, style_id) VALUES (1, 3, 2);
INSERT INTO Orders (metal_id, size_id, style_id) VALUES (2, 4, 1);
INSERT INTO Orders (metal_id, size_id, style_id) VALUES (3, 2, 3);
INSERT INTO Orders (metal_id, size_id, style_id) VALUES (4, 5, 2);
INSERT INTO Orders (metal_id, size_id, style_id) VALUES (5, 1, 1);

-- End block






    -- `type_id` INTEGER NOT NULL,
    -- FOREIGN KEY(`type_id`) REFERENCES `Types`(`id`)
-- CREATE TABLE `Types`
-- (
--     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `type` NVARCHAR(160) NOT NULL,
--     `priceMultiplier` INTEGER NOT NULL
-- )