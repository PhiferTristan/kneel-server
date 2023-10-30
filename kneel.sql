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

    -- `type_id` INTEGER NOT NULL,
    -- FOREIGN KEY(`type_id`) REFERENCES `Types`(`id`)
-- CREATE TABLE `Types`
-- (
--     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `type` NVARCHAR(160) NOT NULL,
--     `priceMultiplier` INTEGER NOT NULL
-- )