CREATE TABLE IF NOT EXISTS chief (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	department varchar(100)
);


CREATE TABLE IF NOT EXISTS employee (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	department varchar(100),
	chief INTEGER NOT NULL REFERENCES chief(id)
);


