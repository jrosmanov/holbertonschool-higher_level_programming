-- using join 
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON states.id = cities.state_id;