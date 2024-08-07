-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id is NULL OR referee_id <> 2