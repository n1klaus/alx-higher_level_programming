-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name as name, SUM(rankings.rate) AS rating
	FROM tv_genres AS g
	LEFT JOIN tv_show_genres as genres
	ON g.id = genres.genre_id
	LEFT JOIN tv_show_ratings AS rankings
	ON genres.show_id = rankings.show_id
	GROUP BY name
	ORDER BY rating DESC;
