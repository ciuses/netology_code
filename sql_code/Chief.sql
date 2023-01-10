CREATE TABLE IF NOT EXISTS employees (
	id SERIAL PRIMARY KEY,
	employee VARCHAR(40) NOT NULL,
	chief VARCHAR(40) UNIQUE,
	department varchar(100)
);

