
CREATE VIEW [users_v1] AS
    SELECT 
        u.uid,
        u.first_name,
        u.last_name,
        u.phone_number,
        u.email,
        u.birthdate,
        u.national_id,
        u.address,
        u.join_date,
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
        Staffs s ON u.uid = s.uid