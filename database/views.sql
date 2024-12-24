USE car_loan;

CREATE VIEW StaffDetails AS
SELECT u.uid, u.first_name, u.last_name, u.email, u.phone_number, u.address, u.birthdate, u.national_id
FROM Users u
JOIN Staff s ON u.uid = s.uid;

CREATE VIEW CustomerDetails AS
SELECT u.uid, u.first_name, u.last_name, u.email, u.phone_number, u.address, u.birthdate, u.national_id
FROM Users u
JOIN Customers c ON u.uid = c.uid;

