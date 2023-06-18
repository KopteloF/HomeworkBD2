# Создание базы данных
createdb -U postgres musicbd

# Вход в управление базой
psql -U postgres -d musicbd

# Создание таблиц
CREATE TABLE genres (
id INT PRIMARY KEY,
name VARCHAR(255)
CONSTRAINT name_genres_unique UNIQUE (name)
);

CREATE TABLE performers (
id INT PRIMARY KEY,
name VARCHAR(255)
CONSTRAINT name_performer_unique UNIQUE (name)
);

CREATE TABLE albums (
id INT PRIMARY KEY,
name VARCHAR(255),
year INT
);

# Ограничение года выпуска
SELECT * FROM albums WHERE year >= 1900;

CREATE TABLE tracks (
id INT PRIMARY KEY,
name VARCHAR(255),
duration INT,
album_id INT,
CONSTRAINT max_track_duration CHECK (duration <= 10800),
FOREIGN KEY (album_id) REFERENCES albums(id)
);

CREATE TABLE compilations (
id INT PRIMARY KEY,
name VARCHAR(255),
year INT
);

# Ограничение года выпуска
SELECT * FROM compilations WHERE year >= 1900;

CREATE TABLE compilation_tracks (
id INT PRIMARY KEY,
track_id INT,
compilation_id INT,
FOREIGN KEY (track_id) REFERENCES tracks(id),
FOREIGN KEY (compilation_id) REFERENCES compilations(id)
);

# Связующая таблица для отношения многие-ко-многим между таблицами genres и performers:

CREATE TABLE performer_genres (
performer_id INT,
genre_id INT,
PRIMARY KEY (performer_id, genre_id),
FOREIGN KEY (performer_id) REFERENCES performers(id),
FOREIGN KEY (genre_id) REFERENCES genres(id)
);

# Связующая таблица для отношения многие-ко-многим между таблицами performers и albums:

CREATE TABLE performer_albums (
performer_id INT,
album_id INT,
CONSTRAINT performer_album_pk PRIMARY KEY (performer_id, album_id),
FOREIGN KEY (performer_id) REFERENCES performers(id),
FOREIGN KEY (album_id) REFERENCES albums(id)
);