CREATE TABLE Staffs (
    uid UNIQUEIDENTIFIER PRIMARY KEY,
    FOREIGN KEY (uid) REFERENCES Users(uid)
);

-- Step 1: Drop existing foreign key constraints
ALTER TABLE Staffs
DROP CONSTRAINT FK__Staffs__uid__160F4887;  -- Replace with the actual constraint name if known


-- Step 2: Recreate foreign key constraints with ON DELETE CASCADE
ALTER TABLE Staffs
ADD CONSTRAINT FK__Staffs__uid__Users
FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE;

