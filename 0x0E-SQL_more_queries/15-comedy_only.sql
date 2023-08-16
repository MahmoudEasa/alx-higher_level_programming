-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT t.title
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg ON g.id = sg.genre_id
INNER JOIN tv_shows AS t ON sg.show_id = t.id
WHERE g.name = 'Comedy'
ORDER BY t.title ASC;

