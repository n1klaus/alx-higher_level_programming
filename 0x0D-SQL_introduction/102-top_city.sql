-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
ALTER TABLE temperatures
	ADD COLUMN temp1 float
	ADD COLUMN temp2 float
	ADD COLUMN avg_temp float AS ((temp1 + temp2) / 2);
SELECT city, avg_temp
        FROM temperatures
	SET temp1 =
	        (SELECT AVG(value)
		FROM temperatures
		WHERE month = 7)
                GROUP BY city
	SET temp2 =
		(SELECT AVG(value)
		FROM temperatures
		WHERE month = 8
		GROUP BY city)
        ORDER BY avg_temp DESC;
