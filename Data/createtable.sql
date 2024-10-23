DROP TABLE IF EXISTS anime_table;

CREATE TABLE anime_table(
    MAL_ID int,
    Title VARCHAR(100),
    Score float,
    Genre VARCHAR(125),
    AnimeType VARCHAR(7),
    AnimeLength int,
    AirDate VARCHAR(28),
    Producers VARCHAR(375),
    Studio VARCHAR(80),
    Source VARCHAR(13),
    Duration VARCHAR(21),
    Rating VARCHAR(30),
    Popularity int
)


-- create table test_table as (select * from anime_table limit 10);