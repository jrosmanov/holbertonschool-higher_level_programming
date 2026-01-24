-- count
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres s ON g.id = s.genre_id
GROUP BY g.id, g.name
ORDER BY number_of_shows DESC;