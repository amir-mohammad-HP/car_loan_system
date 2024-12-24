USE car_loan;

CREATE PROCEDURE AddStaff
    @uid INT,
    @first_name VARCHAR(50),
    @last_name VARCHAR(50),
    @join_date DATE,
    @email VARCHAR(100),
    @phone_number VARCHAR(15),
    @address VARCHAR(255),
    @birthdate DATE,
    @national_id VARCHAR(20)
AS
BEGIN
    INSERT INTO Users (uid, first_name, last_name, join_date, email, phone_number, address, birthdate, national_id)
    VALUES (@uid, @first_name, @last_name, @join_date, @email, @phone_number, @address, @birthdate, @national_id);
    
    INSERT INTO Staff (uid)
    VALUES (@uid);
END;

CREATE PROCEDURE AddCustomer
    @first_name VARCHAR(50),
    @last_name VARCHAR(50),
    @email VARCHAR(100),
    @phone_number VARCHAR(15),
    @address VARCHAR(255),
    @birthdate DATE,
    @national_id VARCHAR(20)
AS
BEGIN
    DECLARE @NewUID TABLE (uid INT);

    INSERT INTO Users (first_name, last_name, email, phone_number, address, birthdate, national_id)
    OUTPUT INSERTED.uid INTO @NewUID
    VALUES (@first_name, @last_name, @email, @phone_number, @address, @birthdate, @national_id);

    INSERT INTO Customers (uid)
    VALUES (SELECT uid FROM @NewUID);
END;

CREATE PROCEDURE AddCar
    @uid INT,
    @model VARCHAR(50),
    @car_production_year INT,
    @license_plate VARCHAR(20),
    @color VARCHAR(20),
    @hourly_price DECIMAL(10, 2),
    @status VARCHAR(20)
AS
BEGIN
    INSERT INTO Cars (uid, model, car_production_year, license_plate, color, hourly_price, status)
    VALUES (@uid, @model, @car_production_year, @license_plate, @color, @hourly_price, @status);
END;

CREATE PROCEDURE AddReservation
    @customer_uid INT,
    @car_uid INT,
    @start_date DATE,
    @end_date DATE,
    @status VARCHAR(20)
AS
BEGIN
    INSERT INTO Reservations (customer_uid, car_uid, start_date, end_date, status)
    VALUES (@customer_uid, @car_uid, @start_date, @end_date, @status);
END;

CREATE PROCEDURE DeleteCar
    @uid INT
AS
BEGIN
    DELETE FROM Cars WHERE uid = @uid;
END;

CREATE PROCEDURE DeleteReservation
    @customer_uid INT,
    @car_uid INT
AS
BEGIN
    DELETE FROM Reservations WHERE customer_uid = @customer_uid AND car_uid = @car_uid;
END;
