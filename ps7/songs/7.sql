SELECT AVG() FROM songs WHERE artist_id IN
(SELECT id FROM artists WHERE name IS "Drake");