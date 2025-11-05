-- Active: 1762236704066@@127.0.0.1@3306
PRAGMA table_info ('orders')

-- 기존에 생성해둔 테이블
-- customers 테이블 생성: 고객 정보를 저장하기 위한 테이블
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- 고객 ID (기본 키)
    name TEXT,                      -- 고객 이름 (텍스트 타입)
    email TEXT,                     -- 고객 이메일 (텍스트 타입)
    phone TEXT                      -- 고객 전화번호 (텍스트 타입)
);

-- customers 테이블에 데이터 삽입
INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),    -- 허균 고객 정보
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),  -- 김영희 고객 정보
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');    -- 이철수 고객 정보


-- 1. orders 테이블 삭제
DROP TABLE orders;

-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
-- 2. 요구사항대로 수정(customer과의 관계 설정)하여 재생성
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL,               -- 총 주문 금액 (실수 타입)
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

-- 3. order 테이블 수정
-- orders 테이블에 Integer 타입의 price 컬럼 추가한다. 
ALTER TABLE
    orders
ADD COLUMN
    price INTEGER;

-- orders 테이블의 total_amount 컬럼을 삭제한다.
ALTER TABLE
    orders 
DROP COLUMN
    total_amount;

-- 4.orders 테이블에 데이터 삽입
-- SQLite에서는 정수형 컬럼이어도 실수형을 입력하면 입력이 됨.
INSERT INTO orders (customer_id, order_date, price) VALUES
    (1, '2023-07-15', 50.99),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, '2023-07-16', 75.50),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, '2023-07-17', 30.25);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25


-- 5. orders의 모든 데이터를 조회한다. 
-- 단, 관계를 맺고 있는 customers의 name도 함께 출력한다.(JOIN사용)
SELECT
    orders.order_id,
    customers.name,
    orders.order_date,
    orders.price
FROM
    orders 
INNER JOIN customers
    ON orders.customer_id = customers.customer_id;