-- Script that lists shows that don't belong to the Comedy genre
SELECT tv_shows.title -- Query to get shows excluding comedies
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title -- Query to get Comedy shows
	FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
) AS comedy_shows
ON tv_shows.title = comedy_shows.title
WHERE comedy_shows.title IS NULL;

