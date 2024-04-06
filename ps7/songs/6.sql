SELECT name FROM songs WHERE artist_id IN
(SELECT movie_id FROM ratings WHERE name IS "Post Malone");