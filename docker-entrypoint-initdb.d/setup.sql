CREATE DATABASE IF NOT EXISTS base;

REVOKE ALL PRIVILEGES ON *.* FROM 'admin'@'%';
GRANT ALL ON *.* TO 'admin'@'%';

FLUSH PRIVILEGES;

USE base; 

CREATE TABLE IF NOT EXISTS requests (
  id int primary key auto_increment,
  requested_at datetime,
  ip varchar(25),
  host varchar(255),
  requested_path varchar(255)
);
