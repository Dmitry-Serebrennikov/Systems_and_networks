CREATE DATABASE IF NOT EXISTS cdn;
use cdn;

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    filename VARCHAR(255) NOT NULL,
    server VARCHAR(255) NOT NULL
);

INSERT INTO images (filename, server) VALUES
('img1.jpg', '1'),
('img2.jpg', '1'),
('img3.jpg', '2'),
('img4.jpg', '2'),
('img5.jpg', '3');