-- sql file with no name
SELECT s.title, g.genre_id
FROM tv_shows s
JOIN tv_show_genres 
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;