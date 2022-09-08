-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT shows.title AS title, SUM(rankings.rate) AS rating
	FROM tv_shows as shows
	LEFT JOIN tv_show_ratings as rankings
	ON shows.id = rankings.show_id
	GROUP BY title
	ORDER BY rating DESC;
