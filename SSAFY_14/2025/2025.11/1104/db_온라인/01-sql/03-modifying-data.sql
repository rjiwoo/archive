-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createAT DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO
    articles (title, content, createAT)
VALUES
    ('hello', 'world', '2000-01-01');


INSERT INTO
    articles (title, content, createAT)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');

INSERT INTO
    articles (title, content, createAT)
VALUES
    ('mytitle', 'mycontent', DATE());

    
-- 2. Update data in table


-- 3. Delete data from table

-- 심화
