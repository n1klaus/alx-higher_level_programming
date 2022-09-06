-- lists all records with name value from the table second_table in desc order
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC, name DESC;
