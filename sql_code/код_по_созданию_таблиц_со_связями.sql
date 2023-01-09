CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	genres_name VARCHAR(60) NOT NULL
);


CREATE TABLE IF NOT EXISTS artists (
	id SERIAL PRIMARY KEY,
	artists_name VARCHAR(60) NOT NULL
);



CREATE TABLE IF NOT EXISTS genres_artists (
	genres_id INTEGER REFERENCES genres(id),
	artists_id INTEGER REFERENCES artists(id),
	CONSTRAINT pk_genres_artists PRIMARY KEY (genres_id, artists_id)
);



CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	album_name VARCHAR(60) NOT NULL,
	album_data INTEGER
);



CREATE TABLE IF NOT EXISTS artists_albums (
	artists_id INTEGER REFERENCES artists(id),
	album_id INTEGER REFERENCES albums(id),
	CONSTRAINT pk_artists_albums PRIMARY KEY (artists_id, album_id)
);


CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	track_name VARCHAR(80) NOT NULL,
	track_duration TIME,
	album_id INTEGER REFERENCES albums(id)
);


CREATE TABLE IF NOT EXISTS collection (
	id SERIAL PRIMARY KEY,
	сollection_name VARCHAR(80) NOT NULL,
	сollection_date INTEGER
);


CREATE TABLE IF NOT EXISTS tracks_collection (
	tracks_id INTEGER REFERENCES tracks(id),
	collection_id INTEGER REFERENCES collection(id),
	CONSTRAINT pk_tracks_collection PRIMARY KEY (tracks_id, collection_id)
);
