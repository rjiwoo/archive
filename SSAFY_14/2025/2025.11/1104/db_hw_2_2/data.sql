-- Active: 1762234499096@@127.0.0.1@3306

PRAGMA table_info('orders');
SELECT * FROM orders;

PRAGMA table_info('customers'); 
SELECT * FROM customers;

-- orders 테이블을 생성
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE,
    total_amount REAL
);

-- orders 테이블에 서로 다른 데이터를 최소 3개 이상 삽입
INSERT INTO 
    orders (order_id, order_date, total_amount)
VALUES
    ('1', '2023-07-15', '50.99'),
    ('2', '2023-07-16', '75.5'),
    ('3', '2023-07-17', '30.25');

-- customers 테이블을 생성
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT
);

-- customers 테이블에 서로 다른 데이터를 최소 3개 이상 삽입
INSERT INTO 
    customers (customer_id, name, email, phone)
VALUES
    ('1', '허균', 'hong.gildong@example.com', '010-1234-5678'),
    ('2', '김영희', 'kim.younghee@example.com', '010-9876-5432'),
    ('3', '이철수', 'lee.cheolsu@example.com', '010-5555-4444');

-- 데이터 수정
-- orders의 3번째 레코드를 삭제하시오.
DELETE FROM
    orders
WHERE
    order_id = 4;

-- customers의 1번째 레코드의 name을 '홍길동'으로 수정하시오.
UPDATE 
    customers
SET
    name = '홍길동'
WHERE
    customer_id = 1;

-- 데이터 조회
-- orders와 customers의 모든 데이터를 조회하시오.
SELECT * FROM orders;
SELECT * FROM customers;