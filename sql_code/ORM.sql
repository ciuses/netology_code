--TRUNCATE publisher, book, stock CASCADE;

INSERT INTO publisher
VALUES (1, 'ДМК Пресс'),
	(2, 'ООО Издательство «Питер»');

INSERT INTO book
VALUES (1, 'Рогов Е. В. "PostgreSQL изнутри."', 1),
	(2, 'Бизли Д., Джонс Б. К. "Python. Книга рецептов."', 1),
	(3, 'Мэтиз Эрик "Изучаем Python. Программирование игр, визуализация данных, веб-приложения."', 2);

INSERT INTO shop
VALUES (1, 'Буказавр'),
	(2, 'Книжбургер');

INSERT INTO stock
VALUES (1, 1, 1, 100),
	(2, 2, 1, 500),
	(3, 3, 2, 201);

SELECT *
FROM shop
FULL JOIN stock ON shop.id = id_shop
FULL JOIN book ON book.id = id_book
FULL JOIN publisher ON publisher.id = id_publisher
WHERE  publisher."name"='ДМК Пресс';
