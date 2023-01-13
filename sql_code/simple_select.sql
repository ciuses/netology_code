SELECT album_name, album_data
FROM albums
WHERE album_data = 2018;

--SELECT track_name, track_duration
--FROM tracks
--WHERE track_duration = (SELECT max(track_duration) FROM tracks);

SELECT track_name, track_duration
FROM tracks
ORDER BY track_duration DESC
LIMIT 1;

SELECT track_name
FROM tracks
WHERE track_duration > '3:30';

SELECT сollection_name
FROM collection
--WHERE сollection_date IN (2018, 2019, 2020);
--WHERE сollection_date >= 2018 AND сollection_date <= 2020;
WHERE сollection_date BETWEEN 2018 AND 2020;


SELECT artists_name
FROM artists
WHERE artists_name NOT LIKE '% %';


--SELECT track_name
--FROM tracks
--WHERE track_name LIKE '%My%' OR track_name LIKE '%ма%';

SELECT track_name
FROM tracks
WHERE string_to_array(lower(track_name), ' ') && ARRAY['my', 'a'];