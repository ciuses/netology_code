SELECT genres_name, count(artists_id)
FROM genres gen
LEFT JOIN genres_artists ga ON gen.id = ga.genres_id
GROUP BY genres_name;


SELECT album_name, count(track_name)
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.album_id
WHERE album_data BETWEEN 2019 AND 2020
GROUP BY album_name;


SELECT album_name, avg(track_duration)
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.album_id
GROUP BY album_name;


SELECT DISTINCT artists_name
FROM artists art
LEFT JOIN artists_albums ar_al ON	art.id = ar_al.artists_id
LEFT JOIN albums al ON al.id = ar_al.album_id
WHERE album_data != 2020;

SELECT DISTINCT сollection_name
FROM artists art
LEFT JOIN artists_albums ar_al ON art.id = ar_al.artists_id
LEFT JOIN albums al ON al.id = ar_al.album_id
LEFT JOIN tracks tr ON tr.album_id = al.id
LEFT JOIN tracks_collection tc ON tc.tracks_id = tr.id
LEFT JOIN collection col ON col.id = tc.collection_id
WHERE artists_name = 'rammstein';

SELECT album_name, count(ga.genres_id)
FROM genres gen
FULL JOIN genres_artists ga ON gen.id = ga.genres_id
FULL JOIN artists art ON ga.artists_id = art.id
FULL JOIN artists_albums aa ON aa.artists_id = art.id
FULL JOIN albums al ON al.id = aa.album_id
GROUP BY album_name
HAVING count(ga.genres_id) > 1;


SELECT track_name
FROM collection col
FULL JOIN tracks_collection tc ON col.id = tc.collection_id
FULL JOIN tracks tra ON tra.id = tc.tracks_id
WHERE сollection_name IS NULL;


SELECT artists_name, min(track_duration)
FROM artists art
LEFT JOIN artists_albums ar_al ON art.id = ar_al.artists_id
LEFT JOIN albums al ON al.id = ar_al.album_id
LEFT JOIN tracks tra ON tra.album_id = al.id
GROUP BY artists_name;


SELECT album_name, count(album_id)
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.album_id
GROUP BY album_name
HAVING count(album_id) = (SELECT DISTINCT count(album_id) FROM albums al LEFT JOIN tracks tr ON al.id = tr.album_id GROUP BY album_id LIMIT 1);
