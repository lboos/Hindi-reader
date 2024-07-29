CREATE DATABASE hindi;
ALTER DATABASE hindi CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use hindi;

CREATE TABLE hindi_lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    word_dev NVARCHAR(30), /* word in Devanagari */
    pos NVARCHAR(30), /* part of speech */
    word_eng VARCHAR(30), /* word translation in English */
    definition NVARCHAR(255), /* word definition in Devanagari */
    PRIMARY KEY (id)
);

INSERT INTO hindi_lexicon
    (word_dev, pos, word_eng, definition)

VALUES
    (N'स्कूल', NULL, 'school', NULL),
    (N'पहला', NULL, 'first', NULL),
    (N'दन', NULL, 'day', NULL),
    (N'मेरे', NULL, 'my', NULL),
    (N'दोत', NULL, 'friend or friends', NULL),
    (N'आम', NULL, 'mango', NULL),
    (N'का', NULL, 'possessive identifier', NULL),
    (N'पेड़', NULL, 'tree', NULL)
;