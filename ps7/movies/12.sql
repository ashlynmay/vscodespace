SELECT tile FROM movies WHERE movie_id IN
(SELECT movie_id)