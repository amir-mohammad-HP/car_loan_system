CREATE TABLE Cars (
    uid UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    model NVARCHAR(50) NOT NULL,
    car_production_year INT NULL,
    license_plate VARCHAR(20) NOT NULL,
    color NVARCHAR(20) NULL,
    hourly_price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (
        status IN ('Avalable', 'Unavalable')
    ) NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
);