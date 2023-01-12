--INSERT INTO artists(artists_name)
--VALUES('rammstein');

--DELETE FROM artists;


INSERT INTO artists
VALUES (1, 'rammstein'),
	(2, 'madonna'),
	(3, 'the prodigy'),
	(4, 'кино'),
	(5, 'eminem'),
	(6, 'алла пугачёва'),
	(7, 'joe dassin'),
	(8, 'иога́нн себастья́н бах');

INSERT INTO genres
VALUES (1, 'industrial metal'),
	(2, 'pop'),
	(3, 'electronic music'),
	(4, 'rock'),
	(5, 'rap'),
	(6, 'chanson'),
	(7, 'classical music');

INSERT INTO albums
VALUES (1, 'Mutter', 2019),
	(2, 'Sehnsucht', 1997),
	(3, 'Like a Virgin', 1984),
	(4, 'Music', 2020),
	(5, 'The Fat of the Land', 1997),
	(6, 'Worlds on Fire', 2018),
	(7, 'Звезда по имени Солнце', 1989),
	(8, 'Ночь', 2018),
	(9, 'The Eminem Show', 2002),
	(10, 'The Slim Shady LP', 1999),
	(11, 'Зеркало души', 1978),
	(12, 'То ли ещё будет…', 2020),
	(13, 'Les Champs-Elysees', 1969),
	(14, 'Le Jardin du Luxembourg', 1976),
	(15, 'The Greatest Hits', 2020),
	(16, '100 Лучших Произведений', 2019);


INSERT INTO tracks
VALUES (1, 'Sonne', 4:33, 1),
	(2, 'Ich will', 3:37, 1),
	(3, 'Links 2 3 4', 3:37, 1),
	(4, 'Engel', 4:25, 2),
	(5, 'Stripped', 4:26, 2),
	(6, 'Du Hast', 3:55, 2),
	(7, 'Like a Virgin', 3:39, 3),
	(8, 'Over and Over', 4:12, 3),
	(9, 'Nobodys Perfect', 4:59, 4),
	(10, 'What It Feels Like for a Girl', 4:44, 4),
	(11, 'Funky Shit', 5:16, 5),
	(12, 'Smack My Bitch Up', 5:43, 5),
	(13, 'Mindfields', 5:40, 5),
	(14, 'Voodoo People', 3:46, 6),
	(15, 'Their Law (Live)', 5:29, 6),
	(16, 'Место для шага вперёд', 3:40, 7),
	(17, 'Звезда по имени Солнце', 3:46, 7),
	(18, 'Пачка сигарет', 4:29, 7),
	(19, 'Мама Анархия', 2:47, 8),
	(20, 'Последний герой', 2:17, 8),
	(21, 'Soldier', 3:47, 9),
	(22, 'Say What You Say', 5:10, 9),
	(23, 'My Name Is [Explicit]', 4:29, 10),
	(24, 'Im Shady', 3:32, 10),
	(25, 'If I Had', 4:05, 10),
	(26, 'Волшебник-недоучка', 3:22, 11),
	(27, 'Всё могут короли', 3:05, 11),
	(28, 'Женщина, которая поёт', 4:15, 11),
	(29, 'Улетай, туча', 4:58, 12),
	(30, 'Ты возьми меня с собой', 2:50, 12),
	(31, 'Les Champs-Élysées', 2:39, 13),
	(32, 'Le Petit Pain au chocolat', 3:22, 13),
	(33, 'Le café des trois colombes', 4:00, 14),
	(34, 'À toi', 4:33, 14),
	(35, 'Воздух на струне соль', 5:42, 15),
	(36, 'Fugue in G minor', 3:15, 15),
	(37, 'Токката и фуга', 9:09, 16),
	(38, 'Бранденбургские концерты', 4:03, 16);


INSERT INTO collection
VALUES (1, 'Europe', 2011),
	(2, 'USA', 2009),
	(3, 'Rock', 2017),
	(4, 'Pop', 2021),
	(5, 'Russian collection', 2018),
	(6, 'Foreign songs', 2020),
	(7, 'Dance', 2014),
	(8, 'Only Music', 2007);


INSERT INTO genres_artists
VALUES (1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(2, 6),
	(6, 7),
	(7, 8);


INSERT INTO artists_albums
VALUES (1, 1),
	(1, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 6),
	(4, 7),
	(4, 8),
	(5, 9),
	(5, 10),
	(6, 11),
	(6, 12),
	(7, 13),
	(7, 14),
	(8, 15),
	(8, 16);


INSERT INTO tracks_collection
VALUES (2, 1),
	(11, 1),
	(16, 1),
	(32, 1),
	(7, 2),
	(13, 2),
	(21, 2),
	(4, 3),
	(15, 3),
	(17, 3),
	(37, 3),
	(10, 4),
	(28, 4),
	(26, 5),
	(27, 5),
	(28, 5),
	(29, 5),
	(30, 4),
	(16, 5),
	(17, 5),
	(18, 5),
	(19, 5),
	(5, 6),
	(9, 6),
	(14, 6),
	(24, 6),
	(33, 6),
	(37, 6),
	(38, 7),
	(7, 7),
	(12, 7),
	(24, 7),
	(31, 7),
	(35, 8),
	(36, 8),
	(37, 8),
	(38, 8),
	(11, 8),
	(12, 8),
	(13, 8),
	(14, 8),
	(15, 8);












