SELECT title FROM movies WHERE id IN
(SELECT )
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;