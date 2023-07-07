-- зайти внутрь контейнера
docker exec -it postgres_movies bash

-- войти в plsql shell
psql -U postgres


-- \c converter;  - Это именно когда базы с фильмами добавляются в DATABASE для конвертации
\c converter;



drop table film_workmovie CASCADE;
CREATE TABLE film_workmovie (
    id            UUID PRIMARY KEY,
    title         TEXT,
    description   TEXT,
    creation_date DATE,
--    certificate   TEXT,
    file_path     TEXT,
    rating        FLOAT,
    type          VARCHAR(20),
    created_at    TIMESTAMP WITH TIME ZONE,
    updated_at    TIMESTAMP WITH TIME ZONE
);

drop table genre CASCADE;
CREATE TABLE genre (
    id          UUID PRIMARY KEY,
    name        TEXT,
    description TEXT,
    created_at  TIMESTAMP WITH TIME ZONE,
    updated_at  TIMESTAMP WITH TIME ZONE
);

drop table genre_film_work CASCADE;
CREATE TABLE genre_film_work (
    id           UUID PRIMARY KEY,
    film_work_id UUID,
    genre_id     UUID,
    created_at   TIMESTAMP WITH TIME ZONE,

    CONSTRAINT fk_film_work_id FOREIGN KEY(film_work_id) REFERENCES film_workmovie(id),
    CONSTRAINT fk_genre_id FOREIGN KEY(genre_id) REFERENCES genre(id)
);

drop table person CASCADE;
CREATE TABLE person (
    id         UUID PRIMARY KEY,
    full_name  VARCHAR(50),
--    birth_date DATE,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);


drop table person_film_work CASCADE;
CREATE TABLE person_film_work (
    id           UUID PRIMARY KEY,
    film_work_id UUID,
    person_id    UUID,
    role         TEXT,
    created_at   TIMESTAMP WITH TIME ZONE,
    CONSTRAINT fk_person_film_work_id FOREIGN KEY(film_work_id) REFERENCES film_workmovie(id),
    CONSTRAINT fk_person_id FOREIGN KEY(person_id) REFERENCES person(id)
);
