-- List all genres from DB and display the number of shows linked to each genre
SELECT tv_show_genres.name AS genre, COUNT(*) number_of_shows
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
