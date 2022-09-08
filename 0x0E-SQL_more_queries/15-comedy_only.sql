-- lists all comedy shows in the database hbtn_0d_tvshows
SELECT tv.title AS title
	FROM tv_shows AS tv
	INNER JOIN tv_show_genres AS genres
	ON tv.id = genres.show_id
	INNER JOIN tv_genres AS shows
	ON shows.id = genres.genre_id
	WHERE shows.name = 'Comedy'
	ORDER BY title ASC;
