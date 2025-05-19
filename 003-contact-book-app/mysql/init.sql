CREATE DATABASE IF NOT EXISTS contactbook;
USE contactbook;

CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO contacts (name, address, phone, email) VALUES 
('João', 'Avenida da Liberdade', '1234-567', 'joaon@example.com'),
('Maria', 'Avenida Egas Moniz', '8901-234' ,'maria@example.com'),
('Luís', 'Avenida do Combatente', '5678-901', 'luisexample.com');
