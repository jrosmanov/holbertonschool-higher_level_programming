-- WELCOME TO CALIFORNIA THE DREAMLAND!!!
SELECT id, name FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name='California'
);