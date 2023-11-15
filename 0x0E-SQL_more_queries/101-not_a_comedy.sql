-- List all shows without the genre 'Comedy'.
-- This script selects the title from tv_shows where the title is not in the subquery result,
-- which retrieves titles of shows with the genre 'Comedy' by an inner join between tv_shows and tv_show_genres.
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
      SELECT s.title
      FROM tv_shows s
      INNER JOIN tv_show_genres tsg ON s.id = tsg.show_id
      INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
      WHERE tg.name = 'Comedy');

