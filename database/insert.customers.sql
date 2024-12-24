

DECLARE @NewUID TABLE (uid UNIQUEIDENTIFIER);

INSERT INTO Users (first_name, last_name, email, phone_number, address, birthdate, national_id)
OUTPUT INSERTED.uid INTO @NewUID
VALUES 
-- (@first_name, @last_name, @email, @phone_number, @address, @birthdate, @national_id)
('amir mohammad', 'hamidi', NULL, '09387932922', NULL, '2000-09-11', '0925366049');

-- Declare a variable to hold the uid
DECLARE @uid UNIQUEIDENTIFIER;

-- Select the uid from the @NewUID table
SELECT @uid = uid FROM @NewUID;

-- Now insert into Customers using the retrieved uid
INSERT INTO Customers (uid)
VALUES (@uid);
