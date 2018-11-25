---- If *not* installing from scratch,
---- uncomment these lines to get a clean database setup.
--DROP DATABASE django IF EXISTS;
--DROP USER 'django'@'localhost' IF EXISTS;

CREATE DATABASE IF NOT EXISTS 'django';
CREATE USER IF NOT EXISTS 'django'@'localhost' IDENTIFIED BY -- 'uncomment and insert your strong database password here';
GRANT ALL PRIVILEGES ON 'django'.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
