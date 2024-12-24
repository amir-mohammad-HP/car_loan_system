IF NOT EXISTS (SELECT * FROM sys.views WHERE name = 'users_v1')
BEGIN
    EXEC('CREATE VIEW [users_v1] AS
    SELECT 
        u.first_name,  -- Assuming the column is named first_name
        CASE 
            WHEN c.uid IS NOT NULL THEN 1 
            ELSE 0 
        END AS is_customer,
        CASE 
            WHEN s.uid IS NOT NULL THEN 1 
            ELSE 0 
        END AS is_staff
    FROM 
        Users u
    LEFT JOIN 
        Customers c ON u.uid = c.uid
    LEFT JOIN 
        Staffs s ON u.uid = s.uid;');
END
