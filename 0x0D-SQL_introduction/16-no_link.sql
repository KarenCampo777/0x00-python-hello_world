-- This script list all records with an ordered by score name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;