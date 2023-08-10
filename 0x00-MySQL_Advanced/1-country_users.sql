-- creating a user table
-- these are the attributes name, id, email, country
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225) NOT NULL,
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
