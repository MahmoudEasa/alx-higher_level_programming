-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g
WHERE g.id NOT IN
	(
		SELECT sg.genre_id
		FROM tv_show_genres AS sg
		INNER JOIN tv_shows AS s ON sg.show_id = s.id
		WHERE s.title = 'Dexter'
	)
ORDER BY g.name ASC;

