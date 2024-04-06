SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM stars WHERE )
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;