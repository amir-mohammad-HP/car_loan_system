
CREATE VIEW [cars_v1] AS
    SELECT 
        c.uid,
        c.model,
        c.car_production_year,
        c.license_plate,
        c.color,
        c.hourly_price,
        c.status,
        c.created_at
    FROM 
        cars c;