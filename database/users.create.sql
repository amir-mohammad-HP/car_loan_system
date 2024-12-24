CREATE TABLE Users (
    uid UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    join_date DATE DEFAULT GETDATE(),
    email VARCHAR(100) NULL,
    phone_number VARCHAR(15) NOT NULL,
    address NVARCHAR(255) NULL,
    birthdate DATE NOT NULL,
    national_id VARCHAR(20) NOT NULL UNIQUE,
);

ALTER TABLE [dbo].[Users] WITH CHECK 
ADD 
CONSTRAINT [CK_NOT_BE_NULL_first_name] CHECK ([first_name] <> N''),
CONSTRAINT [CK_NOT_BE_NULL_last_name] CHECK ([last_name] <> N''),
CONSTRAINT [CK_NOT_BE_NULL_phone_number] CHECK ([phone_number] <> N''),
CONSTRAINT [CK_NOT_BE_NULL_birthdate] CHECK ([birthdate] <> N''),
CONSTRAINT [CK_NOT_BE_NULL_national_id] CHECK ([national_id] <> N'');