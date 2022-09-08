-- lists all genres from hbtn_0d_tvshows of the show Dexter
SELECT genres.name AS name
	FROM tv_genres AS genres
	INNER JOIN tv_show_genres AS shows
	ON genres.id = shows.genre_id
	INNER JOIN tv_shows AS tv
	ON tv.id = shows.show_id
	WHERE tv.title = 'Dexter'
	ORDER BY name ASC;
