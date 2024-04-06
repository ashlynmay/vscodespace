SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM stars WHERE person_id IN
(SELECT ))
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;