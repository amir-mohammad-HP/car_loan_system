CREATE PROCEDURE AddUser
    @first_name VARCHAR(50),
    @last_name VARCHAR(50),
    @email VARCHAR(100),
    @phone_number VARCHAR(15),
    @address VARCHAR(255),
    @birthdate DATE,
    @national_id VARCHAR(20)
AS
BEGIN
    INSERT INTO Users (first_name, last_name, email, phone_number, address, birthdate, national_id)
    VALUES (@first_name, @last_name, @email, @phone_number, @address, @birthdate, @national_id);
END;

-- ***************************************************************************************************
CREATE PROCEDURE AddUserWithRoleCheck
    @first_name VARCHAR(50),
    @last_name VARCHAR(50),
    @email VARCHAR(100),
    @phone_number VARCHAR(15),
    @address VARCHAR(255),
    @birthdate DATE,
    @national_id VARCHAR(20),
    @is_customer BIT,
    @is_staff BIT
AS
BEGIN
    DECLARE @NewUID TABLE (uid UNIQUEIDENTIFIER);
    DECLARE @uid UNIQUEIDENTIFIER;

    -- Insert the new user and capture the inserted uid
    INSERT INTO Users (first_name, last_name, email, phone_number, address, birthdate, national_id)
    OUTPUT INSERTED.uid INTO @NewUID
    VALUES (@first_name, @last_name, @email, @phone_number, @address, @birthdate, @national_id);

    -- Get the newly inserted uid
    SELECT @uid = uid FROM @NewUID;

    -- Handle customer role
    IF @is_customer = 1
        BEGIN
            -- Insert into Customers table
            INSERT INTO Customers (uid)
            VALUES (@uid);
        END

    -- Handle staff role
    IF @is_staff = 1
        BEGIN
            -- Insert into Staffs table
            INSERT INTO Staffs (uid)
            VALUES (@uid);
        END
END;

-- **************************************************************************************************************
CREATE PROCEDURE EditUserWithRole
    @uid UNIQUEIDENTIFIER,
    @first_name VARCHAR(50),
    @last_name VARCHAR(50),
    @email VARCHAR(100),
    @phone_number VARCHAR(15),
    @address VARCHAR(255),
    @birthdate DATE,
    @national_id VARCHAR(20),
    @is_customer BIT,
    @is_staff BIT
AS
BEGIN

    -- Update the existing user
    UPDATE Users
        SET 
            first_name = @first_name,
            last_name = @last_name,
            email = @email,
            phone_number = @phone_number,
            address = @address,
            birthdate = @birthdate,
            national_id = @national_id
        WHERE uid = @uid;
        
    -- Handle customer role
    IF @is_customer = 1
        BEGIN
            -- Insert into Customers table
            INSERT INTO Customers (uid)
            VALUES (@uid);
        END
    ELSE
        BEGIN
            -- If the user is not a customer, check if they exist in the Customers table and delete
            IF EXISTS (SELECT 1 FROM Customers WHERE uid = @uid)
            BEGIN
                DELETE FROM Customers WHERE uid = @uid;
            END
        END

    -- Handle staff role
    IF @is_staff = 1
        BEGIN
            -- Insert into Staffs table
            INSERT INTO Staffs (uid)
            VALUES (@uid);

        END
    ELSE
        BEGIN
            -- If the user is not staff, check if they exist in the Staffs table and delete
            IF EXISTS (SELECT 1 FROM Staffs WHERE uid = @uid)
            BEGIN
                DELETE FROM Staffs WHERE uid = @uid;
            END
        END
END;

