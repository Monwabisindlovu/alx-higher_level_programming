-- Use the database
USE hbtn_0d_tvshows_rate;

-- Select shows and their rating sum
SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
