SELECT name FROM movies WHERE artist_id IN
(SELECT movie_id FROM ratings WHERE rating = 10.0);