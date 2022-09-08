-- lists all shows, and all genres linked to that show from the database hbtn_0d_tvshows
SELECT tv.title AS title, shows.name AS name
	FROM tv_shows AS tv
	LEFT JOIN tv_show_genres AS genres
	ON tv.id = genres.show_id
	LEFT JOIN tv_genres AS shows
	ON shows.id = genres.genre_id
	ORDER BY title ASC, name ASC;
