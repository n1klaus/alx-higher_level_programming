-- lists number of records with same score from the table second_table in desc order
SELECT score, COUNT(score) AS number FROM second_table
	GROUP BY score
	ORDER BY number DESC;
