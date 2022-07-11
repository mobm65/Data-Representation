use film;

create table classifyfilm(
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(250),
    director varchar(250),
    filmgenre varchar (250),
    filmclassification varchar (250)
);

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(1, 'Dr Who', 'Annetta Laufer', 'science fiction', 'g');

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(2, 'Daleks Invasion Earth', 'Gordon Flemyng', 'science fiction', 'pg');

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(3, 'Good Luck To You', 'Sophie Hand', 'comedy', 'sixteen');

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(4, 'Pleasure', 'Ninja Thyberg', 'drama', 'eighteen');

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(5, 'The Lost Girls', 'Livia De Paolis', 'fantasy', 'twelve advisory');

INSERT INTO classifyfilm(id, name, director, filmgenre, filmclassification)
VALUES(6, 'Lightyear', 'Angus MacLane', 'action adventure', 'pg');
