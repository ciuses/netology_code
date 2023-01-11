CREATE TABLE IF NOT EXISTS employees (
	id SERIAL PRIMARY KEY,
	employee VARCHAR(40) NOT NULL,
	chief INTEGER REFERENCES employees(id),
	department VARCHAR(100)
);

