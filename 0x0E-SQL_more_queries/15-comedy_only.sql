-- List all show titles that belong to the genre 'Comedy' by joining tv_shows, tv_show_genres, and tv_genres.
-- The result is filtered using WHERE to include only shows with the genre 'Comedy' and is ordered by title.
SELECT ts.title
FROM tv_shows AS ts
JOIN tv_show_genres AS tgs ON ts.id = tgs.show_id
JOIN tv_genres AS tgg ON tgs.genre_id = tgg.id
WHERE tgg.name = 'Comedy'
GROUP BY ts.title ASC;

