#### 난이도

😵  🤔



## SELECT

#### 모든 레코드 조회

~~~sql
SELECT * FROM ANIMAL_INS
~~~

#### 역순 정렬

~~~SQL
SELECT NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC
~~~

#### 아픈 동물 찾기

~~~mysql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = "Sick"
~~~

#### 어린 동물 찾기  🤔

~~~SQL
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE NOT INTAKE_CONDITION IN ("Aged") 
ORDER BY ANIMAL_ID
~~~

#### 동물의 아이디와 이름

~~~~sqlite
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
~~~~

#### 여러 기준으로 정렬하기 

~~~~SQL
SELECT ANIMAL_ID, NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY NAME, DATETIME DESC
~~~~

#### 상위 N개 레코드 🤔

~~~~SQL
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1 
~~~~

## SUM, MAX, MIN

#### 최댓값 구하기

~~~sql
SELECT DATETIME AS 시간 FROM ANIMAL_INS
ORDER BY DATETIME DESC 
LIMIT 1

----
SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS
~~~

#### 최솟값 구하기

~~~sql
SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS
~~~

#### 동물 수 구하기

~~~sql
SELECT COUNT(*) FROM ANIMAL_INS
~~~

#### 중복 제거하기

~~~sql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS 

----
SELECT COUNT(DISTINCT NAME) AS NAME_COUNT 
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
~~~

## GROUP BY

#### 고양이와 개는 몇 마리 있을까

~~~~sql

~~~~

#### 동명 동물 수 찾기

~~~~sql

~~~~

#### 입양 시각 구하기 1

~~~~sql

~~~~

#### 입양 시각 구하기 2

~~~~sql

~~~~

## IS NULL

#### 이름이 없는 동물의 아이디

~~~~sql

~~~~

#### 이름이 있는 동물의 아이디

~~~~sql

~~~~

#### NULL 처리하기

~~~~sql

~~~~

## JOIN

#### 없어진 기록 찾기

~~~~sql

~~~~

#### 있었는데요 없었습니다

~~~~sql

~~~~

#### 오랜 기간 보호한 동물 1

~~~~sql

~~~~

#### 보호소에서 중성화한 동물

~~~~sql

~~~~

## String, Date

#### 루시와 엘라 찾기

~~~~sql

~~~~

#### 이름에 el이 들어가는 동물 찾기

~~~~sql

~~~~

#### 중성화 여부 파악하기

~~~~sql

~~~~

#### 오랜 기간 보호한 동물 2

~~~~sql

~~~~

#### DATETIME에서 DATE로 형 변환

~~~~sql

~~~~

