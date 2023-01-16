--DROP TABLE phone_numbers;
--DROP TABLE clients;

CREATE TABLE IF NOT EXISTS clients (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(60) NOT NULL,
	last_name VARCHAR(80) NOT NULL,
	email VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS phone_numbers (
	phone_id INTEGER REFERENCES clients(id),
	phone_number VARCHAR(20)
);

--TRUNCATE clients, phone_numbers CASCADE;

INSERT INTO clients
VALUES (1, 'Фёдор', 'Дядя', 'fedor@df_city.com'),
	(2, 'Матроскин', 'Кот', 'matroskin@df_city.com'),
	(3, 'Шарик', 'Пёс', 'sharick@df_city.com'),
	(4, 'Галчёнок', 'Кто Там','jackdaw@village.com'),
	(5, 'Игорь Иванович', 'Печкин', 'pechkin@village.com');

INSERT INTO phone_numbers
VALUES (1, '79019011234'),
	(2, '79029017776'),
	(3, '79039014862'),
	(4, '79049019559'),
	(5, '79059016666'),
	(1, '79019011111'),
	(1, '79019013333'),
	(1, '79777777777'),
	(1, '79019011523');


SELECT *
FROM clients
FULL JOIN phone_numbers ON id = phone_id;
