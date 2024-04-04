SELECT title FROM songs WHERE id IN
(SELECT id FROM artist )