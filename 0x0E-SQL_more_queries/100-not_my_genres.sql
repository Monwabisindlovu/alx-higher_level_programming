-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- This script selects the name from tv_genres where the genre name is not in the subquery result,
-- which retrieves genres linked to the show Dexter by an inner join between tv_genres and tv_show_genres.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
      (SELECT tv_genres.name
      FROM tv_genres
      INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
      INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = "Dexter");
