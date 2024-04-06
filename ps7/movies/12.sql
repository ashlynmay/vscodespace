SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM stars WHERE
)