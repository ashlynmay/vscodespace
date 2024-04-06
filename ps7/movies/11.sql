SELECT title FROM movies WHERE movie_id 
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;