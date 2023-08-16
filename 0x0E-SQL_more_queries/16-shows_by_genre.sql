-- Lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows
SELECT s.title,
	COALESCE(g.name, NULL) AS name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
ORDER BY s.title, g.name ASC;

