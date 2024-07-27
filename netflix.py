import sqlite3
import pandas as pd

# Load the CSV file
file_path = '/Users/brahamnoorsingh/Desktop/Tableau-Dashboards-info/netflix_titles.csv'
df = pd.read_csv(file_path)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('netflix_titles.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS netflix_titles (
    show_id TEXT,
    type TEXT,
    title TEXT,
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added TEXT,
    release_year INTEGER,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
)
''')

# Insert the CSV data into the table
df.to_sql('netflix_titles', conn, if_exists='replace', index=False)

# Define SQL queries
queries = [
    "SELECT title, director, release_year FROM netflix_titles;",
    "SELECT * FROM netflix_titles WHERE release_year > 2015;",
    "SELECT country, COUNT(*) as count FROM netflix_titles GROUP BY country;",
    "SELECT * FROM netflix_titles ORDER BY release_year DESC;",
    "SELECT type, COUNT(*) as count FROM netflix_titles GROUP BY type;",
    "SELECT AVG(CAST(SUBSTR(duration, 1, LENGTH(duration)-4) AS INTEGER)) as avg_duration FROM netflix_titles WHERE type = 'Movie';",
    "SELECT DISTINCT rating FROM netflix_titles;",
    "SELECT country, COUNT(*) as count FROM netflix_titles GROUP BY country ORDER BY count DESC LIMIT 5;",
    "SELECT strftime('%Y', date(date_added)) as year, COUNT(*) as count FROM netflix_titles GROUP BY year ORDER BY year;",
    "SELECT * FROM netflix_titles WHERE type = 'TV Show';",
    "SELECT rating, COUNT(*) as count FROM netflix_titles WHERE type = 'TV Show' GROUP BY rating;",
    "SELECT AVG(CAST(SUBSTR(duration, 1, LENGTH(duration)-8) AS INTEGER)) as avg_seasons FROM netflix_titles WHERE type = 'TV Show';",
    "SELECT title, duration FROM netflix_titles WHERE type = 'TV Show' ORDER BY CAST(SUBSTR(duration, 1, LENGTH(duration)-8) AS INTEGER) DESC LIMIT 5;",
    """DELETE FROM netflix_titles
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM netflix_titles
        GROUP BY title, type
    );"""
]

# Execute and display the results of the SQL queries
for query in queries:
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"Query: {query}")
    for row in result:
        print(row)
    print("\n")

# Commit changes and close the connection
conn.commit()
conn.close()
