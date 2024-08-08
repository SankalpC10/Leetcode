-- Write your PostgreSQL query statement below
Select eu.unique_id, e.name
FROM Employees e LEFT JOIN EmployeeUNI eu
ON e.id = eu.id