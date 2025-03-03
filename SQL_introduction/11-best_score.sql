-- List all records of a table with specific condition in descending score order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
