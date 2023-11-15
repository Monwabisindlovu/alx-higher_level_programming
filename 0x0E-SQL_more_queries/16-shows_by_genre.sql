-- List all shows and their genres, including those without genres, ordered by show title and genre name.
-- This script selects the title from tv_shows, and the genre name from tv_genres using left joins with tv_show_genres
-- based on the show and genre IDs. It orders the result by show title and genre name.
SELECT ts.title, tgg.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tgs ON ts.id = tgs.show_id
LEFT JOIN tv_genres AS tgg ON tgs.genre_id = tgg.id
ORDER BY ts.title, tgg.name;

