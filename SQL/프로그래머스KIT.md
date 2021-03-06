#### ๋์ด๋

๐ต  ๐ค



## SELECT

#### ๋ชจ๋  ๋ ์ฝ๋ ์กฐํ

~~~sql
SELECT * FROM ANIMAL_INS
~~~

#### ์ญ์ ์ ๋ ฌ

~~~SQL
SELECT NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC
~~~

#### ์ํ ๋๋ฌผ ์ฐพ๊ธฐ

~~~mysql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = "Sick"
~~~

#### ์ด๋ฆฐ ๋๋ฌผ ์ฐพ๊ธฐ  ๐ค

~~~SQL
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE NOT INTAKE_CONDITION IN ("Aged") 
ORDER BY ANIMAL_ID
~~~

#### ๋๋ฌผ์ ์์ด๋์ ์ด๋ฆ

~~~~sqlite
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
~~~~

#### ์ฌ๋ฌ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌํ๊ธฐ 

~~~~SQL
SELECT ANIMAL_ID, NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY NAME, DATETIME DESC
~~~~

#### ์์ N๊ฐ ๋ ์ฝ๋ ๐ค

~~~~SQL
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1 
~~~~

## SUM, MAX, MIN

#### ์ต๋๊ฐ ๊ตฌํ๊ธฐ ๐ค

~~~sql
SELECT DATETIME AS ์๊ฐ FROM ANIMAL_INS
ORDER BY DATETIME DESC 
LIMIT 1

----
SELECT MAX(DATETIME) AS ์๊ฐ FROM ANIMAL_INS
~~~

#### ์ต์๊ฐ ๊ตฌํ๊ธฐ

~~~sql
SELECT MIN(DATETIME) AS ์๊ฐ FROM ANIMAL_INS
~~~

#### ๋๋ฌผ ์ ๊ตฌํ๊ธฐ

~~~sql
SELECT COUNT(*) FROM ANIMAL_INS
~~~

#### ์ค๋ณต ์ ๊ฑฐํ๊ธฐ ๐ค

~~~sql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS 

----
SELECT COUNT(DISTINCT NAME) AS NAME_COUNT 
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
~~~

## GROUP BY

#### ๊ณ ์์ด์ ๊ฐ๋ ๋ช ๋ง๋ฆฌ ์์๊น ๐ค

~~~~sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
~~~~

#### ๋๋ช ๋๋ฌผ ์ ์ฐพ๊ธฐ ๐ต

~~~~sql
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT >= 2
ORDER BY NAME
~~~~

#### ์์ ์๊ฐ ๊ตฌํ๊ธฐ 1 ๐ต

~~~~sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) > 8 AND HOUR(DATETIME) < 20
GROUP BY HOUR(DATETIME)
ORDER BY 1
~~~~

#### ์์ ์๊ฐ ๊ตฌํ๊ธฐ 2 ๐ต ๐ต

 https://velog.io/@ljs7463/MySQL-%EC%9E%85%EC%96%91-%EC%8B%9C%EA%B0%81-%EA%B5%AC%ED%95%98%EA%B8%B02

SET์ ์ด์ฉํด 0~23์ ํ์ด๋ธ์ ์์ฑ

SET์ ์ด๋ค ๊ฐ์ ๋ฃ์ด์ค ๋ ์ฌ์ฉ, @๋ ๋ณ์๋ช ์์ ์์น, :=๋ ๋์

~~~sql
SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
~~~

COUNTํ ํ์ด๋ธ ์์ฑ

HOUR(DATETIME)= @HOUR ์ผ๋ COUNTํ ๊ฐ์ SELECT ํ๊ฒ ํ๋ค.

~~~~sql
SET @HOUR := -1; # ๋ณ์์ ์ธ

SELECT (@HOUR := @HOUR +1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR < 23

----

~~~~

## IS NULL

#### ์ด๋ฆ์ด ์๋ ๋๋ฌผ์ ์์ด๋

~~~~sql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID
~~~~

#### ์ด๋ฆ์ด ์๋ ๋๋ฌผ์ ์์ด๋

~~~~sql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID
~~~~

#### NULL ์ฒ๋ฆฌํ๊ธฐ ๐ค

~~~~sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, 
SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
~~~~

## JOIN

- LEFT JOIN, RIGHT JOIN ๊ธฐ์ค

๊ฒฐ๊ณผ๊ฐ ์ผ์ชฝ ํ์ด๋ธ ์ ์ฒด ๋ฐ์ดํฐ ๋์์ด๋ผ๋ฉด left๋ฅผ ,์ค๋ฅธ์ชฝ ํ์ด๋ธ์ ์ ์ฒด ๋ฐ์ดํฐ๊ฐ ๋์์ด๋ผ๋ฉด right๋ฅผ ์ฌ์ฉํฉ๋๋ค.

- LEFT JOIN : A์ Bํ์ด๋ธ ์กฐ์ธํ๋๋ฐ, B์ ๋งคํ๋๋ ๊ฐ์ด ์๋  ๋ง๋  A๋ ๋ชจ๋ ๋์ด

A left join B on (a.id = b.id)

#### ์์ด์ง ๊ธฐ๋ก ์ฐพ๊ธฐ ๐ต

~~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID FROM ANIMAL_INS
)
   
----
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
~~~~

#### ์์๋๋ฐ์ ์์์ต๋๋ค ๐ต

๋๋ ์กฐ์ธ์ผ๋ก ํ

~~~~sql
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME;
----
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
~~~~

#### ์ค๋ ๊ธฐ๊ฐ ๋ณดํธํ ๋๋ฌผ 1 ๐ต

~~~~sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
~~~~

#### ๋ณดํธ์์์ ์ค์ฑํํ ๋๋ฌผ ๐ต

~~~~sql
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%' 
AND (B.SEX_UPON_OUTCOME LIKE 'Spayed%' 
OR B.SEX_UPON_OUTCOME LIKE'Neutered%')
ORDER BY A.ANIMAL_ID

----

SELECT DISTINCT AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME
FROM ANIMAL_INS AS AI
JOIN ANIMAL_OUTS AS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.SEX_UPON_INTAKE != AO.SEX_UPON_OUTCOME
ORDER BY AI.ANIMAL_ID ASC
~~~~

## String, Date

#### ๋ฃจ์์ ์๋ผ ์ฐพ๊ธฐ

~~~~sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
~~~~

#### ์ด๋ฆ์ el์ด ๋ค์ด๊ฐ๋ ๋๋ฌผ ์ฐพ๊ธฐ

~~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'DOG'
ORDER BY NAME
~~~~

#### ์ค์ฑํ ์ฌ๋ถ ํ์ํ๊ธฐ ๐ค

~~~~sql
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE 'Intact%', 'X', 'O') AS '์ค์ฑํ'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
~~~~

#### ์ค๋ ๊ธฐ๊ฐ ๋ณดํธํ ๋๋ฌผ 2 ๐ค

~~~~sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NOT NULL
ORDER BY A.DATETIME - B.DATETIME
LIMIT 2
~~~~

#### DATETIME์์ DATE๋ก ํ ๋ณํ ๐ค

~~~~sql
SELECT ANIMAL_ID, NAME,  DATE_FORMAT(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
~~~~

