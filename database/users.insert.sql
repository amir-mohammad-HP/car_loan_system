-- Insert rows into table 'car_loan' in schema '[dbo]'
INSERT INTO [dbo].[Users]
( -- Columns to insert data into
    first_name ,
    last_name ,
    phone_number ,
    birthdate ,
    national_id
)
VALUES
( -- First row: values for the columns in the list above
 'amir mohammad', 'hamidi', '09387932922', GETDATE(), '0925366048'
)
-- Add more rows here
GO
