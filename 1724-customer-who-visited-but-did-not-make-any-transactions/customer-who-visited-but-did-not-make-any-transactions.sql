-- Write your PostgreSQL query statement below
Select v.customer_id, count(v.visit_id) as count_no_trans
FROM Visits v left join Transactions t
ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY v.customer_id