-- lists all records of the table second_table with score >= 10 in desc order
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
