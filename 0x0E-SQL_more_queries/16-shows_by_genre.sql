-- List all shows and their corresponding genres.
-- This script selects the title from tv_shows and the name from tv_genres,
-- joining them on tv_show_genres.show_id and tv_shows.id.
SELECT
    tv_shows.title AS title,
    tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id;
