USE car_loan;

-- DECLARE @sql NVARCHAR(MAX) = N'';
-- SELECT @sql += 'DROP TABLE ' + QUOTENAME(s.name) + '.' + QUOTENAME(t.name) + '; '
-- FROM sys.tables AS t
-- INNER JOIN sys.schemas AS s ON t.schema_id = s.schema_id;

-- EXEC sp_executesql @sql;

-- DROP TABLE Logs;
-- DROP TABLE ManageCar;
DROP TABLE Reservations;
DROP TABLE Cars;
DROP TABLE Customers;
-- DROP TABLE Staffs;
DROP TABLE Users;