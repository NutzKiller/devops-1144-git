-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS catgifs;

-- Use the created database
USE catgifs;

-- Create the 'images' table if it doesn't exist
CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
);

-- Insert some sample cat GIF URLs into the 'images' table
INSERT INTO images (url) VALUES
("https://images.dog.ceo/breeds/beagle/n02088364_1128.jpg"),
("https://images.dog.ceo/breeds/pekinese/n02086079_4412.jpg"),
("https://images.dog.ceo/breeds/spaniel-welsh/n02102177_2055.jpg");
