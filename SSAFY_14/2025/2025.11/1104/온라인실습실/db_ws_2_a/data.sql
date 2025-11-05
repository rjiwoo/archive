-- Active: 1762240491000@@127.0.0.1@3306

-- 'artists' 테이블에서 모든 아티스트의 정보를 조회하시오.
select * from artists;

-- 'artists' 테이블의 모든 데이터의 수를 조회하시오.
SELECT count(*) from artists;

-- 'artists' 테이블에서 Name이 'AC/DC' 인 정보를 조회하시오.
select * from artists where Name='AC/DC';

-- 'artists' 테이블의 모든 데이터 중, artistid와 Name만 출력하시오.
select artistid, Name from artists;

-- 'artists' 테이블에서 Name이 'Gilberto Gil' 이거나 'Ed Motta' 정보를 조회하시오.
select * from artists where Name='Gilberto Gil' OR Name='Ed Motta';

-- 'artists' 테이블에서 모든 정보를 Name 기준으로 내림차순 정렬하여 조회하시오.
select * from artists order by Name DESC;

-- 'artists' 테이블에서 이름이 'Vinícius' 로 시작하는 정보를 조회하시오. 단, 2개까지만 출력되도록 한다.
select * from artists where Name LIKE 'Vinícius%' limit 2;

-- 'artists' 테이블에서 'ArtistId'가 50번부터 70번까지의 데이터를 조회하여 'ArtistId'만 출력하시오.
SELECT ArtistId
FROM artists
WHERE ArtistId BETWEEN 50 AND 70;

