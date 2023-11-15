-- Use the hbtn_0d_tvshows database to list all genres of the show Dexter.
-- This script selects genres from the tv_genres table for the show Dexter.
SELECT g.name FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
	AND t.show_id = s.id
	AND s.title = "Dexter"
ORDER BY g.name ASC;
