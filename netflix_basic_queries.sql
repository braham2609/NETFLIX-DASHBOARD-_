
-- Selecting specific columns
SELECT title, director, release_year FROM netflix_titles;

-- Filtering rows based on conditions
SELECT * FROM netflix_titles WHERE release_year > 2015;

-- Aggregating data
SELECT country, COUNT(*) as count FROM netflix_titles GROUP BY country;

-- Sorting results
SELECT * FROM netflix_titles ORDER BY release_year DESC;

-- Example of joining tables (not applicable here)
-- SELECT a.title, b.actor_name FROM netflix_titles a JOIN actors b ON a.show_id = b.movie_id;

-- Counting the number of movies and TV shows
SELECT type, COUNT(*) as count FROM netflix_titles GROUP BY type;

-- Finding the average duration of movies
SELECT AVG(CAST(SUBSTR(duration, 1, LENGTH(duration)-4) AS INTEGER)) as avg_duration 
FROM netflix_titles 
WHERE type = 'Movie';

-- Listing all unique ratings
SELECT DISTINCT rating FROM netflix_titles;

-- Finding the top 5 countries with the most titles
SELECT country, COUNT(*) as count FROM netflix_titles GROUP BY country ORDER BY count DESC LIMIT 5;

-- Getting the number of titles added each year
SELECT strftime('%Y', date(date_added)) as year, COUNT(*) as count 
FROM netflix_titles 
GROUP BY year 
ORDER BY year;


-- Selecting all TV shows
SELECT * FROM netflix_titles WHERE type = 'TV Show';

-- Counting the number of TV shows by rating
SELECT rating, COUNT(*) as count FROM netflix_titles WHERE type = 'TV Show' GROUP BY rating;

-- Finding the average number of seasons for TV shows
SELECT AVG(CAST(SUBSTR(duration, 1, LENGTH(duration)-8) AS INTEGER)) as avg_seasons 
FROM netflix_titles 
WHERE type = 'TV Show';

-- Finding the top 5 TV shows with the most seasons
SELECT title, duration FROM netflix_titles WHERE type = 'TV Show' ORDER BY CAST(SUBSTR(duration, 1, LENGTH(duration)-8) AS INTEGER) DESC LIMIT 5;

-- Removing duplicate titles based on title and type
DELETE FROM netflix_titles
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM netflix_titles
    GROUP BY title, type
);

