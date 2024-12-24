CREATE TABLE Customers (
    uid UNIQUEIDENTIFIER PRIMARY KEY,
    FOREIGN KEY (uid) REFERENCES Users(uid)
);


ALTER TABLE Customers
DROP CONSTRAINT FK__Customers__uid__18EBB532;  -- Replace with the actual constraint name if known

ALTER TABLE Customers
ADD CONSTRAINT FK__Customers__uid__Users
FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE;