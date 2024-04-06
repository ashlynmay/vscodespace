SELECT * FROM movies
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;