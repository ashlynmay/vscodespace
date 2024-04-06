SELECT title FROM movies WHERE id IN (
)
JOIN ratings on movies.id = ratings.movie_id LIMIT 5;