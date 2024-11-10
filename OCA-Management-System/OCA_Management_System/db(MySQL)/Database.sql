CREATE DATABASE oca_management_system;
USE oca_management_system;

CREATE TABLE Events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date DATE,
    status ENUM('Pending', 'Approved', 'Rejected'),
    club_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(50),
    is_booked BOOLEAN DEFAULT FALSE
);
CREATE TABLE Budgets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    club_name VARCHAR(100),
    amount_requested DECIMAL(10, 2),
    status ENUM('Pending', 'Approved', 'Rejected'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Communications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sender VARCHAR(100),
    receiver VARCHAR(100),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE EventAnalytics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    attendance INT,
    feedback_score DECIMAL(3, 2),
    budget_used DECIMAL(10, 2)
);