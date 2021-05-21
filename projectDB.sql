CREATE DATABASE projectDB;
USE projectDB;
CREATE TABLE user(
id INT PRIMARY KEY AUTO_INCREMENT,
login VARACHAR(12),
password VARACHAR(12)
);
SHOW TABLES;
INSERT INTO user (login, password) VALUES ("Jhon" , "1234"),
("Jack", "abcd&");
SELECT * FROM user